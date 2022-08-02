from django.test import TestCase
from django.utils.crypto import get_random_string
from realms.models import Realm, RealmUser
from zentral.contrib.inventory.models import MetaBusinessUnit
from zentral.contrib.mdm.models import ReEnrollmentSession, UserEnrollmentSession
from zentral.contrib.mdm.payloads import build_scep_payload
from .utils import complete_enrollment_session, force_user_enrollment


class TestUserEnrollment(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mbu = MetaBusinessUnit.objects.create(name=get_random_string(12))
        cls.mbu.create_enrollment_business_unit()
        cls.realm = Realm.objects.create(
            name=get_random_string(12),
            backend="ldap",
            username_claim="username",
            email_claim="email",
        )
        username = get_random_string(12)
        email = f"{username}@example.com"
        cls.realm_user = RealmUser.objects.create(
            realm=cls.realm,
            claims={"username": username,
                    "email": email},
            username=username,
            email=email,
        )

    def test_create_user_enrollment_session_no_managed_apple_id(self):
        enrollment = force_user_enrollment(self.mbu, self.realm)
        session = UserEnrollmentSession.objects.create_from_user_enrollment(enrollment)
        self.assertEqual(session.get_enrollment(), enrollment)
        self.assertEqual(session.status, "ACCOUNT_DRIVEN_START")

    def test_user_enrollment_session_scep_payload(self):
        enrollment = force_user_enrollment(self.mbu, self.realm)
        session = UserEnrollmentSession.objects.create_from_user_enrollment(enrollment)
        session.set_account_driven_authenticated_status(self.realm_user)
        session.set_started_status()
        scep_payload = build_scep_payload(session)
        self.assertEqual(scep_payload["PayloadContent"]["Challenge"],
                         enrollment.scep_config.get_challenge_kwargs()["challenge"])

    def test_user_enrollment_reenrollment_session_error(self):
        enrollment = force_user_enrollment(self.mbu, self.realm)
        session = UserEnrollmentSession.objects.create_from_user_enrollment(enrollment)
        with self.assertRaises(ValueError) as cm:
            ReEnrollmentSession.objects.create_from_enrollment_session(session)
        self.assertEqual(cm.exception.args[0], "The enrollment session doesn't have an enrolled device")

    def test_user_enrollment_reenrollment_session(self):
        enrollment = force_user_enrollment(self.mbu, self.realm)
        session = UserEnrollmentSession.objects.create_from_user_enrollment(enrollment)
        session.set_account_driven_authenticated_status(self.realm_user)
        session.set_started_status()
        complete_enrollment_session(session)
        reenrollment_session = ReEnrollmentSession.objects.create_from_enrollment_session(session)
        self.assertEqual(reenrollment_session.get_enrollment(), enrollment)
        self.assertIsNone(reenrollment_session.dep_enrollment)
        self.assertIsNone(reenrollment_session.ota_enrollment)
        self.assertEqual(reenrollment_session.user_enrollment, enrollment)
        self.assertEqual(reenrollment_session.status, ReEnrollmentSession.STARTED)

    def test_user_enrollment_reenrollment_reenrollment_session(self):
        enrollment = force_user_enrollment(self.mbu, self.realm)
        session = UserEnrollmentSession.objects.create_from_user_enrollment(enrollment)
        session.set_account_driven_authenticated_status(self.realm_user)
        session.set_started_status()
        complete_enrollment_session(session)
        reenrollment_session = ReEnrollmentSession.objects.create_from_enrollment_session(session)
        complete_enrollment_session(reenrollment_session)
        reenrollment_session2 = ReEnrollmentSession.objects.create_from_enrollment_session(reenrollment_session)
        self.assertEqual(reenrollment_session2.get_enrollment(), enrollment)
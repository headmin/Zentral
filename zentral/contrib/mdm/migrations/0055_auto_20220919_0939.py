# Generated by Django 3.2.14 on 2022-09-19 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0054_softwareupdate_softwareupdatedeviceid'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueprint',
            name='collect_apps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Managed Only'), (2, 'All')], default=0),
        ),
        migrations.AddField(
            model_name='blueprint',
            name='collect_certificates',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Managed Only'), (2, 'All')], default=0),
        ),
        migrations.AddField(
            model_name='blueprint',
            name='collect_profiles',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Managed Only'), (2, 'All')], default=0),
        ),
        migrations.AddField(
            model_name='blueprint',
            name='inventory_interval',
            field=models.IntegerField(
                default=86400,
                help_text='In seconds, the minimum interval between two inventory collection. '
                          'Minimum 4h, maximum 7d, default 1d.',
                validators=[django.core.validators.MinValueValidator(14400),
                            django.core.validators.MaxValueValidator(604800)]),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='activation_lock_manageable',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='apple_silicon',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='apps_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='bootstrap_token_allowed_for_authentication',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='bootstrap_token_required_for_kext_approval',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='bootstrap_token_required_for_software_update',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='certificates_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='dep_enrollment',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='device_information',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='device_information_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='os_version',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='profiles_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='security_info',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='security_info_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='supervised',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='user_approved_enrollment',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='enrolleddevice',
            name='user_enrollment',
            field=models.BooleanField(null=True),
        ),
    ]
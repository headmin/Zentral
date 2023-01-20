# Generated by Django 3.2.14 on 2023-01-23 17:50

import django.contrib.postgres.fields.ranges
from django.db import migrations


def update_availability(apps, schema_editor):
    SoftwareUpdate = apps.get_model("mdm", "SoftwareUpdate")
    for su in SoftwareUpdate.objects.all():
        su.availability = (su.posting_date, su.expiration_date)
        su.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0057_auto_20230112_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwareupdate',
            name='availability',
            field=django.contrib.postgres.fields.ranges.DateRangeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='softwareupdate',
            unique_together={('platform', 'major', 'minor', 'patch', 'public', 'availability')},
        ),
        migrations.RunPython(update_availability),
        migrations.AlterField(
            model_name='softwareupdate',
            name='availability',
            field=django.contrib.postgres.fields.ranges.DateRangeField(),
        ),
        migrations.RemoveField(
            model_name='softwareupdate',
            name='posting_date',
        ),
        migrations.RemoveField(
            model_name='softwareupdate',
            name='expiration_date',
        ),
    ]

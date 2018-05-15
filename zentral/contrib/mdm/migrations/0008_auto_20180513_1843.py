# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-13 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0007_auto_20180513_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='depdevice',
            options={'ordering': ('serial_number',)},
        ),
        migrations.AlterModelOptions(
            name='depprofile',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='depdevice',
            name='profile_uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
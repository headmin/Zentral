# Generated by Django 3.2.12 on 2022-04-04 07:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='report_heartbeat_timeout',
            field=models.IntegerField(
                default=3600,
                help_text='in seconds, 600 (10 min) → 172800 (2 days)',
                validators=[django.core.validators.MinValueValidator(600),
                            django.core.validators.MaxValueValidator(172800)]
            ),
        ),
    ]

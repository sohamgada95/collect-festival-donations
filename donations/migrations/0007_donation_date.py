# Generated by Django 5.1 on 2024-08-20 14:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_alter_donation_committee_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

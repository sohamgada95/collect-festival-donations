# Generated by Django 5.0.7 on 2024-08-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donation_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

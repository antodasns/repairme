# Generated by Django 3.1.7 on 2021-03-06 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0009_booking_estimation_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='estimation_status',
            new_name='pickupdateconfirm',
        ),
    ]

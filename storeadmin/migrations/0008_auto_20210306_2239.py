# Generated by Django 3.1.7 on 2021-03-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0007_pickup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='appliance_id',
            new_name='pickup_date',
        ),
        migrations.AddField(
            model_name='pickup',
            name='pickup_status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

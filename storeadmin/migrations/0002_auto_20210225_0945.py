# Generated by Django 3.1.7 on 2021-02-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='appliance_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='store_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user_id',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0005_auto_20210227_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedetails',
            name='store_bgimg',
            field=models.ImageField(upload_to='store/'),
        ),
        migrations.AlterField(
            model_name='storedetails',
            name='store_thumbnail',
            field=models.ImageField(upload_to='store/'),
        ),
    ]

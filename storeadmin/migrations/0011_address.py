# Generated by Django 3.1.7 on 2021-03-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0010_auto_20210306_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('landmark', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0014_auto_20210310_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='estimateconfirm',
            new_name='estimategivenconfirm',
        ),
    ]
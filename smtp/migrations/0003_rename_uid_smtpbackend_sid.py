# Generated by Django 4.2.1 on 2023-06-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smtp', '0002_remove_smtpbackend_id_smtpbackend_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smtpbackend',
            old_name='uid',
            new_name='sid',
        ),
    ]

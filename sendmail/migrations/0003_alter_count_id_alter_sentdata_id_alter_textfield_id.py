# Generated by Django 4.2.2 on 2023-07-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0002_auto_20230723_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sentdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 2.2.3 on 2020-01-30 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhawan_app', '0005_auto_20200131_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelcomplaint',
            old_name='booked_by',
            new_name='complainant',
        ),
        migrations.RenameField(
            model_name='hostelroombooking',
            old_name='complainant',
            new_name='booked_by',
        ),
    ]

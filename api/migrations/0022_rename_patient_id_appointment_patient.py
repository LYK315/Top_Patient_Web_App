# Generated by Django 4.1 on 2023-12-07 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_rename_patient_appointment_patient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patient',
        ),
    ]

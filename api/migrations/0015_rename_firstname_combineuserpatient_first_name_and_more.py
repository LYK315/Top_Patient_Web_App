# Generated by Django 4.1 on 2023-12-06 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combineuserpatient',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='combineuserpatient',
            old_name='lastName',
            new_name='last_name',
        ),
    ]

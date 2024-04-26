# Generated by Django 4.1 on 2023-12-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_user_managers_user_firstname_user_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='fname', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='lname', max_length=200),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-01 14:03

import accounts.models
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190228_1041'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('object', accounts.models.CustomUserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
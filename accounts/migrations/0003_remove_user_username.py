# Generated by Django 3.2.7 on 2021-10-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

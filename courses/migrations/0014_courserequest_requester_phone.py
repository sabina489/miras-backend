# Generated by Django 3.2.7 on 2022-01-30 17:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserequest',
            name='requester_phone',
            field=models.CharField(default=9840016500, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phonenumber 9XXXXXXXXX', regex='^9\\d{9}')]),
            preserve_default=False,
        ),
    ]

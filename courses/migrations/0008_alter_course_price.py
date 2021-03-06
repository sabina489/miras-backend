# Generated by Django 3.2.7 on 2021-12-30 10:33

import courses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courserequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0.0, validators=[
                                    courses.validators.validate_positive], verbose_name='price'),
        ),
    ]

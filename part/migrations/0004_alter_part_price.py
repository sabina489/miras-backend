# Generated by Django 3.2.7 on 2021-12-30 10:33

import courses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0003_remove_part_enrolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='price',
            field=models.FloatField(default=0.0, validators=[
                                    courses.validators.validate_positive], verbose_name='price'),
        ),
    ]

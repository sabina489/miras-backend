# Generated by Django 3.2.7 on 2022-01-20 10:16

import courses.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=7, validators=[
                                      courses.validators.validate_positive], verbose_name='price'),
        ),
    ]

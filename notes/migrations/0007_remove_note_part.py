# Generated by Django 3.2.7 on 2022-05-15 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20220130_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='part',
        ),
    ]

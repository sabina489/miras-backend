# Generated by Django 3.2.7 on 2022-05-09 04:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0017_auto_20220506_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='gorkhapatraexam',
            name='date',
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name='date'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_exam_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='feedback',
            field=models.TextField(blank=True, null=True,
                                   verbose_name='feedback'),
        ),
    ]

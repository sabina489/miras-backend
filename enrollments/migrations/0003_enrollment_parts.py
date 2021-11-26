# Generated by Django 3.2.7 on 2021-11-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0003_remove_part_enrolls'),
        ('enrollments', '0002_rename_user_enrollment_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='parts',
            field=models.ManyToManyField(blank=True, related_name='enrolls', to='part.Part', verbose_name='parts'),
        ),
    ]

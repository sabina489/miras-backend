# Generated by Django 3.2.7 on 2021-12-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_alter_option_feedback'),
        ('enrollments', '0003_enrollment_parts'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='exams',
            field=models.ManyToManyField(blank=True, related_name='enrolls', to='exams.Exam', verbose_name='exams'),
        ),
    ]

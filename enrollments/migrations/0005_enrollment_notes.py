# Generated by Django 3.2.7 on 2021-12-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
        ('enrollments', '0004_enrollment_exams'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='notes',
            field=models.ManyToManyField(
                blank=True, related_name='enrolls', to='notes.Note', verbose_name='notes'),
        ),
    ]

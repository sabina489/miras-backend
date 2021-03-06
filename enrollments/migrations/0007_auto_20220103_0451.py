# Generated by Django 3.2.7 on 2022-01-03 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_delete_questionstatus'),
        ('enrollments', '0006_remove_enrollment_exams'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, verbose_name='score')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='exam_states', to='enrollments.enrollment', verbose_name='enrollment')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='exam_states', to='exams.exam', verbose_name='exam')),
            ],
            options={
                'verbose_name': 'ExamStatus',
                'verbose_name_plural': 'ExamStatuss',
            },
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exams',
            field=models.ManyToManyField(blank=True, related_name='enrolls',
                                         through='enrollments.ExamStatus', to='exams.Exam', verbose_name='exams'),
        ),
    ]

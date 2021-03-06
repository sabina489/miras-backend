# Generated by Django 3.2.7 on 2022-01-03 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0007_auto_20220103_0451'),
        ('exams', '0011_auto_20220103_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionstatus',
            name='exam_stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='question_states', to='enrollments.examstatus', verbose_name='exam_stat'),
        ),
    ]

# Generated by Django 3.2.7 on 2022-05-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='how_to_pay',
            field=models.URLField(blank=True, null=True,
                                  verbose_name='how_to_pay'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers_video',
            field=models.URLField(blank=True, null=True,
                                  verbose_name='teachers_video'),
        ),
    ]

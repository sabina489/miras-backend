# Generated by Django 3.2.7 on 2022-05-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0008_alter_examstatus_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='examstatus',
            name='submitted',
            field=models.BooleanField(default=False, verbose_name='submitted'),
        ),
    ]
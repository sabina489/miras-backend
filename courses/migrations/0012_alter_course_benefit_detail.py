# Generated by Django 3.2.7 on 2022-01-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20220119_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='benefit_detail',
            field=models.TextField(blank=True, null=True,
                                   verbose_name='benefit_detail'),
        ),
    ]
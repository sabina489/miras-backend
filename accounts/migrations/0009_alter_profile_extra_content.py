# Generated by Django 3.2.7 on 2022-01-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211227_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='extra_content',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]

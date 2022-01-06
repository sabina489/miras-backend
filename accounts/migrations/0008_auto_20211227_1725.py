# Generated by Django 3.2.7 on 2021-12-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_extra_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
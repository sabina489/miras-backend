# Generated by Django 3.2.7 on 2022-01-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_courserequest_requester_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserequest',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courserequest',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]

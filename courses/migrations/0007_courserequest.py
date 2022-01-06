# Generated by Django 3.2.7 on 2021-12-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, verbose_name='Course Name')),
                ('course_category', models.CharField(max_length=200, verbose_name='Course Category')),
                ('requester_name', models.CharField(max_length=200, verbose_name='Requester Name')),
                ('requester_email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Request', 'Request'), ('Denied', 'Denied')], default='Request', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]

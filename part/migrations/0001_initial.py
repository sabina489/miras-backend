# Generated by Django 3.2.7 on 2021-11-24 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0003_auto_20211121_1131'),
        ('enrollments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('detail', models.TextField(
                    blank=True, null=True, verbose_name='detail')),
                ('price', models.FloatField(default=0.0, verbose_name='price')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='parts', to='courses.course', verbose_name='course')),
                ('enrolls', models.ManyToManyField(related_name='parts',
                 to='enrollments.Enrollment', verbose_name='enrolls')),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
        ),
    ]

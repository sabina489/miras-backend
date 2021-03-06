# Generated by Django 3.2.7 on 2022-05-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0016_alter_mockexam_timer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='mockexam',
            name='level',
            field=models.CharField(default='I', max_length=20),
        ),
        migrations.AddField(
            model_name='mockexam',
            name='officer',
            field=models.ManyToManyField(blank=True, to='exams.Officer'),
        ),
    ]

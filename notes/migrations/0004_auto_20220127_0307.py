# Generated by Django 3.2.7 on 2022-01-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='file',
        ),
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(choices=[('Recorded Video', 'Recorded Video'), ('Others', 'Others')], default='Recorded Video', max_length=20, verbose_name='Type'),
        ),
    ]
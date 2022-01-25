# Generated by Django 3.2.7 on 2022-01-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_price'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='course',
        ),
        migrations.RemoveField(
            model_name='content',
            name='part',
        ),
        migrations.AddField(
            model_name='content',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='notes.note'),
        ),
    ]

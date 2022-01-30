# Generated by Django 3.2.7 on 2022-01-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0004_alter_part_price'),
        ('notes', '0002_note_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='part.part'),
        ),
    ]

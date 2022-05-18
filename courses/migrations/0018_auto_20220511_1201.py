# Generated by Django 3.2.7 on 2022-05-11 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0017_merge_20220511_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courserequest',
            name='requester_email',
        ),
        migrations.RemoveField(
            model_name='courserequest',
            name='requester_name',
        ),
        migrations.RemoveField(
            model_name='courserequest',
            name='requester_phone',
        ),
        migrations.RemoveField(
            model_name='courserequest',
            name='view_count',
        ),
        migrations.RemoveField(
            model_name='courserequest',
            name='vote_count',
        ),
        migrations.AddField(
            model_name='courserequest',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='requests', to='courses.course', verbose_name='course'),
        ),
        migrations.AddField(
            model_name='courserequest',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='course_requests', to='accounts.user', verbose_name='created_by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courserequest',
            name='votes',
            field=models.ManyToManyField(
                related_name='course_requests_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courserequest',
            name='course_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='requests', to='courses.coursecategory', verbose_name='category'),
        ),
    ]
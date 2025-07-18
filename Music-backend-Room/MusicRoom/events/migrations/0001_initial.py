# Generated by Django 5.2.3 on 2025-06-22 20:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('songs', models.JSONField(default=list)),
                ('managers', models.JSONField(default=list)),
                ('track_votes', models.JSONField(default=dict)),
                ('is_public', models.BooleanField(default=True)),
                ('event_start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_end_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attended_events', to='users.user')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to='users.user')),
            ],
            options={
                'db_table': 'events',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['organizer'], name='events_organiz_1c7a2e_idx'), models.Index(fields=['is_public'], name='events_is_publ_cf11db_idx'), models.Index(fields=['event_start_time'], name='events_event_s_7d11ce_idx')],
            },
        ),
    ]

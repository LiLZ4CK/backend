# Generated by Django 5.2.4 on 2025-07-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_bio_user_email_privacy_user_facebook_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='event_notifications',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='user',
            name='playlist_notifications',
            field=models.JSONField(default=dict),
        ),
    ]

# Generated by Django 5.1.6 on 2025-05-16 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_user_id_users_id_users_groups_users_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password_hash',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-03 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_password_reset_email_sent_time',
        ),
    ]
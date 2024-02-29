# Generated by Django 3.2.18 on 2023-04-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0028_auto_20230410_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundraiser',
            name='signup_email_closing',
        ),
        migrations.RemoveField(
            model_name='fundraiser',
            name='signup_email_opening',
        ),
        migrations.RemoveField(
            model_name='fundraiser',
            name='signup_email_subject',
        ),
        migrations.AddField(
            model_name='campaign',
            name='signup_email_closing',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='signup_email_opening',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='signup_email_subject',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
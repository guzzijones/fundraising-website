# Generated by Django 3.2.18 on 2023-04-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0027_auto_20230407_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='about_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='about_title',
            field=models.TextField(blank=True),
        ),
    ]
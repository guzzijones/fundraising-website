# Generated by Django 3.2.18 on 2023-04-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0023_donation_tax_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='default_fundraiser_amount',
            field=models.IntegerField(default=0),
        ),
    ]

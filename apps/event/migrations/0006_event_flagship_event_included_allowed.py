# Generated by Django 4.2.3 on 2023-09-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_terms_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='flagship_event_included_allowed',
            field=models.IntegerField(default=0),
        ),
    ]

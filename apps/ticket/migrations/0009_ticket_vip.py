# Generated by Django 4.2.3 on 2023-10-29 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_ticket_declined'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='vip',
            field=models.BooleanField(default=False),
        ),
    ]

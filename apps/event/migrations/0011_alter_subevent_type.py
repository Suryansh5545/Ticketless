# Generated by Django 4.2.3 on 2023-10-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_event_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subevent',
            name='type',
            field=models.CharField(choices=[('standard', 'Standard'), ('premium', 'Premium'), ('student', 'Student')], default='standard', max_length=100),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-20 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_promocode_email_promocode_email_sended_and_more'),
        ('ticket', '0003_ticket_promo_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='promocode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.promocode'),
        ),
    ]

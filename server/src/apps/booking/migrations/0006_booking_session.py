# Generated by Django 4.2.5 on 2023-10-02 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_bookingsession_alter_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.bookingsession', verbose_name='Сессия'),
        ),
    ]
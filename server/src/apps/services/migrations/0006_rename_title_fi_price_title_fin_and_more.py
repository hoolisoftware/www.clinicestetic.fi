# Generated by Django 4.2.5 on 2023-10-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_price_title_en_us_price_title_fi_price_title_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='title_fi',
            new_name='title_fin',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='title_fi',
            new_name='title_fin',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('prices', models.ManyToManyField(blank=True, to='services.price', verbose_name='Цены')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('image', models.ImageField(upload_to='services/service/image', verbose_name='Изображение')),
                ('prices', models.ManyToManyField(blank=True, to='services.price', verbose_name='Цены')),
            ],
            options={
                'verbose_name': 'Комплекс лечения',
                'verbose_name_plural': 'Комплексы лечения',
            },
        ),
    ]

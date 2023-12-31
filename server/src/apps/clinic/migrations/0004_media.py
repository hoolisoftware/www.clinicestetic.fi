# Generated by Django 4.2.5 on 2023-10-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_clinicconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название соц. сети')),
                ('link', models.URLField(verbose_name='Ссылка на соц. сеть')),
                ('icon', models.ImageField(upload_to='clinic/media/icon/', verbose_name='Иконка соц. сети')),
            ],
            options={
                'verbose_name': 'Соц. сеть',
                'verbose_name_plural': 'Соц. сети',
            },
        ),
    ]

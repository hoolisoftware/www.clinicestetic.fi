# Generated by Django 4.2.5 on 2023-10-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_US',
            field=models.CharField(max_length=64, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fi',
            field=models.CharField(max_length=64, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=64, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en_US',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_fi',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_en_US',
            field=models.TextField(null=True, verbose_name='Короткий контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_fi',
            field=models.TextField(null=True, verbose_name='Короткий контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_ru',
            field=models.TextField(null=True, verbose_name='Короткий контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_US',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fi',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок'),
        ),
    ]
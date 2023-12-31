# Generated by Django 4.2.5 on 2023-10-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_faq_answer_alter_faq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en_US',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fi',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en_US',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fi',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
    ]

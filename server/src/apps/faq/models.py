from django.db import models


class FAQ(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'

    def __str__(self):
        return self.question

from django.db import models


class Record(models.Model):
    created = models.DateTimeField('Создано', auto_now=True)
    status_checked = models.BooleanField('Проверено?', default=False)

    class Meta:
        abstract = True


class BookingSession(models.Model):
    time_start = models.TimeField('Время начала')
    time_end = models.TimeField('Время конца')

    class Meta:
        ordering = ('time_start',)
        verbose_name = 'Сессия приёма'
        verbose_name_plural = 'Сессии приёма'

    def __str__(self):
        return f'{self.time_start} - {self.time_end}'


class Booking(Record):
    full_name = models.CharField('ИФО', max_length=128)
    phone_number = models.CharField('Номер телефона', max_length=64)
    date = models.DateField('Дата приёма')
    session = models.ForeignKey(BookingSession, verbose_name='Сессия', on_delete=models.CASCADE, blank=True, null=True) # noqa

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приём'


class FormFeedback(Record):
    full_name = models.CharField('ИФО', max_length=128)
    phone_number = models.CharField('Номер телефона', max_length=64)
    message = models.TextField('Сообщение', blank=True, null=True)

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'


class FormPhone(Record):
    phone_number = models.CharField('Номер телефона', max_length=64)

    class Meta:
        verbose_name = 'Форма номера телефона'
        verbose_name_plural = 'Формы номера телефона'

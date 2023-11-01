from django.db import models


class Price(models.Model):
    title = models.CharField('Название', max_length=64)
    price = models.IntegerField('Цена', blank=True, null=True, help_text='Заметка: 0 если бесплатно, -1 что бы не показывать цену') # noqa
    parent = models.ForeignKey(verbose_name='Родитель', to='self', on_delete=models.CASCADE, related_name='prices', null=True, blank=True) # noqa
    starting_from = models.BooleanField('Начинается от?', default=False)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ['id']

    def __str__(self):
        return f'{self.title} {self.price if self.price else self.prices.count()}' # noqa


class Service(models.Model):
    title = models.CharField('Название', max_length=64)
    image = models.ImageField('Изображение', upload_to='services/service/image') # noqa
    prices = models.ManyToManyField(verbose_name='Цены', to=Price, blank=True) # noqa

    class Meta:
        verbose_name = 'Комплекс услуг'
        verbose_name_plural = 'Комплексы услуг'
        ordering = ['id']

    def __str__(self):
        return self.title

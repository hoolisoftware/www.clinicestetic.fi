from django.db import models


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ClinicConfig(SingletonModel):
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    phone = models.CharField('Номер телефона', max_length=32)
    phone_raw = models.CharField('Номер телефона (без спец. символов и пробелов)', max_length=32, help_text='Используется для ссылки на звонок') # noqa
    email = models.EmailField('Почта клиники')
    address = models.TextField('Адресс клиники')
    address_link = models.TextField('Ссылка на адресс клиники')

    def __str__(self):
        return 'Настройки'


class Specialist(models.Model):
    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    photo = models.ImageField('Фото', upload_to='clinic/specialist/photo', blank=True, null=True) # noqa
    full_name = models.CharField('ИФО', max_length=64)
    position = models.CharField('Позиция', max_length=64)
    about = models.TextField('Доп информация', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    image = models.ImageField('Изображение', upload_to='clinic/certificate/image/') # noqa
    name = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'

    name = models.CharField('Название соц. сети', max_length=64)
    link = models.URLField('Ссылка на соц. сеть')
    icon = models.ImageField('Иконка соц. сети', upload_to='clinic/media/icon/') # noqa

    def __str__(self):
        return self.name


class BeforeAfterUnit(models.Model):
    class Meta:
        verbose_name = 'До и после (фото)'
        verbose_name_plural = 'До и после (фото)'
        ordering = ['id']

    image = models.ImageField('Фотография до и после', upload_to='clinic/before-after-unit/image/') # noqa
    name = models.CharField('Название', max_length=128, help_text='Не обязательно, не показывается нигде кроме админ панели') # noqa

    def __str__(self):
        return self.name


class BeforeAfterSection(models.Model):
    class Meta:
        verbose_name = 'До и после (секция)'
        verbose_name_plural = 'До и после (секции)'
        ordering = ['id']

    title = models.CharField('Заголовок', max_length=64)
    units = models.ManyToManyField(verbose_name='Изображения', to=BeforeAfterUnit, blank=True) # noqa

    def __str__(self):
        return self.title

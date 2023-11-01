from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название', max_length=64)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True) # noqa ignore
    image = models.ImageField('Изображение', upload_to='blog/post/image/')
    title = models.CharField('Заголовок', max_length=128)
    content = models.TextField('Контент')
    excerpt = models.TextField('Короткий контент')
    categories = models.ManyToManyField(verbose_name='Категории', to=Category, blank=True) # noqa ignore
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

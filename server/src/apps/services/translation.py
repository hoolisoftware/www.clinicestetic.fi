from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Price)
class PriceTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', )

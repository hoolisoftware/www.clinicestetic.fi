from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'about')

from django.contrib import admin

from . import models


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer'
    )

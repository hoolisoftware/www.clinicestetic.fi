from django.contrib import admin

from . import models


class PriceInline(admin.TabularInline):
    model = models.Price


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    inlines = ((
        PriceInline,
    ))
    exclude = ('parent',)
    list_display = (
        'title',
        'price'
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

from django.contrib import admin

from . import models


@admin.register(models.BookingSession)
class BookingSessionAdmin(admin.ModelAdmin):
    list_display = (
        'time_start',
        'time_end'
    )


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone_number',
        'date',
        'created',
        'status_checked'
    )


@admin.register(models.FormFeedback)
class FormFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'created',
        'status_checked'
    )


@admin.register(models.FormPhone)
class FormPhoneAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'created',
        'status_checked'
    )

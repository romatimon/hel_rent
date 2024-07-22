from django.contrib import admin
from .models import Helicopter, Applications


@admin.register(Helicopter)
class HelicopterAdmin(admin.ModelAdmin):
    # fields = ['name', 'description', 'passenger', 'range', 'speed', 'rent_price', 'status', 'category']
    list_display = ('name', 'passenger_capacity', 'range', 'speed', 'rent_price', 'status')
    list_display_links = ('name',)  # кликабельные надписи
    ordering = ['passenger_capacity', 'range', 'speed', 'rent_price']
    list_editable = ('status',)  # редактируемое поле
    list_per_page = 10  # пагинация
    # search_fields = ['name', 'category__name']
    # list_filter = ['status', 'category__name']


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'number_phone', 'email', 'number_of_passengers', 'helicopter', 'date_create']
    list_per_page = 10
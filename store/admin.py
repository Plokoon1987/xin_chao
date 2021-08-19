from django.contrib import admin
from . import models

@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'weight', 'rations',
                    'price_per_weight')

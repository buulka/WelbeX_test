from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list = ('date',
            'name',
            'count',
            'distance')



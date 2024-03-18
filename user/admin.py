from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available','image']
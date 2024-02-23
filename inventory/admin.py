from django.contrib import admin
from .models import inventory


class inventoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')

# Register your models here.
admin.site.register(inventory, inventoryAdmin)

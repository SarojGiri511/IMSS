from django.contrib import admin
from .models import product


class productAdmin(admin.ModelAdmin):
    list_display = ('name','sku', 'quantity', 'price', 'thumbnail')

# Register your models here.
admin.site.register(product, productAdmin)

# Admin Django Changes
admin.site.site_title = 'IMS Title'
admin.site.site_header = 'Inventory Management System'
admin.site.index_title = 'Index Title'
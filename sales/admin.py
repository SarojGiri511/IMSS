from django.contrib import admin
from .models import sales

class salesAdmin(admin.ModelAdmin):
    list_display = ('name','address')

# Register your models here.
admin.site.register(sales, salesAdmin)
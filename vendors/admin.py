from django.contrib import admin
from .models import vendors

class vendorsAdmin(admin.ModelAdmin):
    list_display = ('name','address')

# Register your models here.
admin.site.register(vendors, vendorsAdmin)
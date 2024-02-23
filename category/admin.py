from django.contrib import admin
from .models import category


class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')

# Register your models here.
admin.site.register(category, categoryAdmin)
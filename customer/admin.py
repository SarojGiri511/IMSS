from django.contrib import admin
from.models import customer


class customerAdmin(admin.ModelAdmin):
    list_display = ("fname","lname")

# Register your models here.
admin.site.register(customer, customerAdmin)


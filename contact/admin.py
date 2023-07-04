from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',

@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    
# Register your models here.

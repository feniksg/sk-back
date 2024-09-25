from django.contrib import admin

from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at", 'title')

@admin.register(models.OrderCategory)
class OrderCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

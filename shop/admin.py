from msilib import Feature

from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class FeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'inventory', 'new_price', 'created']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'updated']
    inlines = [ImageInline, FeatureInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

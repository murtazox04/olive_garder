from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Category, Food

@admin.register(Category)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Food)
class FoodAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto">')
        return "No Image"

    image_tag.short_description = 'Image'

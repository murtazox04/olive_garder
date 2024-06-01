from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name',)

from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Menu

admin.site.register(Menu, ModelAdmin)

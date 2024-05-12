from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import FoodCategory, Food

admin.site.register(FoodCategory, ModelAdmin)
admin.site.register(Food, ModelAdmin)

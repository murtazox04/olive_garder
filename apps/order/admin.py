from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Order

admin.site.register(Order, ModelAdmin)

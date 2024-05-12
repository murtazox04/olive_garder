from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import CartItem, Cart

admin.site.register(CartItem, ModelAdmin)
admin.site.register(Cart, ModelAdmin)
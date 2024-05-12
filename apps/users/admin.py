from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User, UserGeolocation


class UserAdmin(ModelAdmin):
    list_display = ('username', 'phone_number', 'telegram_id')
    search_fields = ('username', 'phone_number')
    list_filter = ('is_staff', 'is_active')


class UserGeolocationAdmin(ModelAdmin):
    list_display = ('user', 'lat', 'lng', 'reference_point', 'created_at', 'updated_at')
    search_fields = ('user__username', 'reference_point')
    list_filter = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(UserGeolocation, UserGeolocationAdmin)

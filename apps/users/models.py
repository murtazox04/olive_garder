from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=16, unique=True)
    telegram_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserGeolocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
    reference_point = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_geolocation'
        verbose_name = 'User Geolocation'
        verbose_name_plural = 'User Geolocation'
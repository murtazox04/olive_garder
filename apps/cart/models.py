from django.db import models

from apps.users.models import User
from apps.food.models import Food


class CartItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food.name

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    @property
    def total_cost(self):
        return self.food.price * self.quantity


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

from rest_framework import serializers

from .models import Cart, CartItem
from apps.food.models import Food


class CartItemSerializer(serializers.ModelSerializer):
    food_name = serializers.ReadOnlyField(source='food.name')
    food_price = serializers.ReadOnlyField(source='food.price')
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'food', 'food_name', 'food_price', 'quantity', 'total_cost', 'created_at', 'updated_at']
        read_only_fields = ['food_name', 'food_price', 'total_cost', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

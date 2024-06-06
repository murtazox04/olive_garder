from rest_framework import serializers

from .models import Category, Food


class ChildCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    foods = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'children', 'foods']

    def get_children(self, obj):
        children = obj.children.all()
        return ChildCategorySerializer(children, many=True).data if children.exists() else None

    def get_foods(self, obj):
        foods = obj.food_set.all()
        return FoodSerializer(foods, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['children'] is not None:
            data.pop('foods', None)
        return data

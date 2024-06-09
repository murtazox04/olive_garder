from rest_framework import generics, response
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Category, Food
from .serializers import CategorySerializer, FoodSerializer


@method_decorator(cache_page(60 * 15), name='dispatch')
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer


@method_decorator(cache_page(60 * 15), name='dispatch')
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        name = self.kwargs['name']
        return get_object_or_404(Category, name=name)


@method_decorator(cache_page(60 * 15), name='dispatch')
class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        category_name = request.query_params.get('category_name')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


@method_decorator(cache_page(60 * 15), name='dispatch')
class FoodDetailView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_object(self):
        name = self.kwargs['name']
        return get_object_or_404(Food, name=name)

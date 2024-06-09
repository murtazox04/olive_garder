from django.urls import path

from .views import CategoryListView, CategoryDetailView, FoodListView, FoodDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<str:name>/', CategoryDetailView.as_view(), name='category-detail'),
    path('', FoodListView.as_view(), name='food-list'),
    path('<str:name>/', FoodDetailView.as_view(), name='food-detail'),
]

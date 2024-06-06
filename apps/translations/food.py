from modeltranslation.translator import TranslationOptions, register

from apps.food.models import Category, Food


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

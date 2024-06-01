from modeltranslation.translator import TranslationOptions, register

from apps.food.models import FoodCategory, Food


@register(FoodCategory)
class FoodCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

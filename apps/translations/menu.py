from modeltranslation.translator import TranslationOptions, register

from apps.menu.models import Menu


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)

from django.contrib import admin

from .models import Product, Ruler
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Отображение в админ
    list_display = ('id', 'title_product', 'ruler', 'price')
    list_display_links = ('id', 'title_product')
    # Возможность редактировать полей не входя(Обязательно не должно совпадать с
    # первым полем отображения)
    list_editable = ('ruler', 'price')
    search_fields = ('id',)




@admin.register(Ruler)
class RulerAdmin(admin.ModelAdmin):
    list_display = ('name_ruler',)

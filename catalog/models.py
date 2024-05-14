from django.db import models

# Create your models here.


class Product(models.Model):
    title_product = models.CharField(max_length=200, verbose_name='Название роз')
    ruler = models.ForeignKey('ruler', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Из какой линейки')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(verbose_name='Фото карточки', upload_to='product')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.title_product


class Ruler(models.Model):
    name_ruler = models.CharField(max_length=100, verbose_name='Название линейки')

    class Meta:
        verbose_name = "Линейка"
        verbose_name_plural = "Линейки"


    def __str__(self):
        return self.name_ruler
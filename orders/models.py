from django.db import models
from catalog.models import Product

# Create your models here.

class Order(models.Model):
    name_order = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=250)
    email = models.EmailField(verbose_name='email')
    status = models.ForeignKey('status', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Статус', default='Оставлено')
    created = models.DateTimeField(auto_now_add=True)
    id_products = models.CharField(max_length=500, verbose_name='Список id товаров', default="default title")
    price_all_products = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Общая цена', default=1.11)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name_order





class Status(models.Model):
    name_status = models.CharField(max_length=50, verbose_name='Статус', default='Оставлена')

    def __str__(self):
        return self.name_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
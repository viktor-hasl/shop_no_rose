# Generated by Django 5.0.4 on 2024-05-10 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(default='Оставлена', max_length=50, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_order', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_products', models.CharField(default='default title', max_length=500, verbose_name='Список id товаров')),
                ('price_all_products', models.DecimalField(decimal_places=2, default=1.11, max_digits=20, verbose_name='Общая цена')),
                ('status', models.ForeignKey(blank=True, default='Оставлено', null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
    ]

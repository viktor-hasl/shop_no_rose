from django.contrib import admin
from .models import Order, Status
# Register your models here.

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):

    list_display = ['name_order', 'id', 'email',
                    'address', 'created', 'status']
    list_filter = ['id', 'status', 'created']
    list_editable = ['status']
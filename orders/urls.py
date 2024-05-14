from django.urls import path
from .views import order_render, order_request


urlpatterns = [
    path('',  order_render, name='order'),
    path('done', order_request, name='order_request' )
]
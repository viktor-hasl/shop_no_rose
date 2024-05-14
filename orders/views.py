from django.shortcuts import render
from django.conf import settings
from decimal import Decimal
from .models import Order
import requests
from .tg_bot import urls_request
# Create your views here.

def order_render(request):
    req = requests.get(urls_request)
    return render(request, 'order/order.html')


def order_request(request):
    # Переменная для определения отправили ли данные
    no_done = False
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    email = request.POST.get("email")
    cart = (request.session[settings.CART_SESSION_ID])
    price = Decimal('0.0')
    id_product = ''
    if name and phone and address and email and cart:
        for key in cart.keys():
            price += Decimal(cart[key]['price']) * Decimal(cart[key]['quantity'])
            id_product += f'id: {key}({cart[key]["quantity"]}шт.) '


        order = Order(name_order=name, phone=phone, address=address, email=email, status_id=1, id_products=id_product, price_all_products=price)
        order.save()
        del request.session[settings.CART_SESSION_ID]
        txt_tg = f'{name} оставил заявку, его номер {phone}.'
        req = requests.get(urls_request + txt_tg)

    else:
        no_done = True
    return render(request, 'order/order_done.html', {'no': no_done})
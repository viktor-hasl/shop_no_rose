from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    # Получаем все продукты и выводим их в шаблон
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'index.html', {'products': products,
                                          'cart_product_form': cart_product_form
                                          })



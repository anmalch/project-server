from django.shortcuts import render

from products.models import Product, ProductCategory


# контролеры=функции (подключаем их в urls.py в path())
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Catalogue',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)

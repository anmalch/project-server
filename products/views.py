from django.shortcuts import render

from products.models import Product, ProductCategory


# контролеры=функции (подключаем их в urls.py в path())
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Catalogue',
        'categories': ProductCategory.objects.all()
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all() #тернарный оператор можно добавить и в контекст, но будет объемно
    #if category_id:  # если category_id не None, то формируем products
        #category = ProductCategory.objects.get(id=category_id) не обязательно объявлять category, в джанго можно указать доп параметром (category_id=category_id), вместо (category=category)
        #products = Product.objects.filter(category_id=category_id)  # фильтруем по категории
    #else:
        #products = Product.objects.all()
    context['products'] = products  # обновляем контекст

    return render(request, 'products/products.html', context)

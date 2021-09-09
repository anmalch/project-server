from django.shortcuts import render
from django.views.generic.base import TemplateView

from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# контролеры=функции (подключаем их в urls.py в path())

class ProductsTemplateView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        return context


def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop - Catalogue',
        'categories': ProductCategory.objects.all()
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()  # тернарный оператор можно добавить и в контекст, но будет объемно
    # if category_id:  # если category_id не None, то формируем products
    # category = ProductCategory.objects.get(id=category_id) не обязательно объявлять category, в джанго можно указать доп параметром (category_id=category_id), вместо (category=category)
    # products = Product.objects.filter(category_id=category_id)  # фильтруем по категории
    # else:
    # products = Product.objects.all()
    # context['products'] = products  # обновляем контекст

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from products.models import Product, ProductCategory


# контролеры=функции (подключаем их в urls.py в path())

class ProductsTemplateView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        return context


class ProductsListView(TemplateView):
    template_name = 'products/products.html'

    def get_context_data(self, category_id=None, page=1, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Catalogue'
        context['categories'] = ProductCategory.objects.all()

        products = Product.objects.filter(
            category_id=category_id) if category_id else Product.objects.all()  # тернарный оператор можно добавить и в контекст, но будет объемно

        paginator = Paginator(products, per_page=3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context['products'] = products_paginator

        return context

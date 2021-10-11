from django.views.generic.base import TemplateView
from products.models import Product, ProductCategory
from common.views import CommonContextMixin
from django.views.generic.list import ListView
from django.conf import settings
from django.core.cache import cache



def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'GeekShop'


class ProductsListView(CommonContextMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'GeekShop - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = get_links_menu
        return context

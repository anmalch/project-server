from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='product'), #при переходе в каталог, срабатывает url-адрес: /products
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'), #логика отвечает за пагинацию

]
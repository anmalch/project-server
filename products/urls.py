from django.urls import path

from products.views import ProductsListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product'),  # при переходе в каталог, срабатывает url-адрес: /products
    path('<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='page'),  # логика отвечает за пагинацию
]

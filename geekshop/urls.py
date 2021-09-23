from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('baskets/', include('baskets.urls', namespace='baskets')),
    path('admin-staff/', include('admins.urls', namespace='admins')),
    path('', include('social_django.urls', namespace='social')),
]

# проверка, что работаем локально (обратимся к переменной Debug (settings.py), она стоит в значение True,
# это означает что мы радотаем локально
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

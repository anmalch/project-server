from django.urls import path

from admins.views import index, UserListView, UserCreateView, UserUpdateView, admin_users_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'), #вместо id теперь пердаем pk(primary key)
    path('users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
]
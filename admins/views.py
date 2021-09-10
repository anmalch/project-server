from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


#@user_passes_test(lambda u: u.is_staff)  # обращаемся к польз-ю и проверяем, если user is_staff, то доступны контроллеры
#def index(request):
#   context = {'title': 'GeekShop - Admin'}
#   return render(request, 'admins/index.html', context)  # возвращается генерация шаблона


class UserTemplateView(TemplateView):
    template_name = 'admins/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):  # метод, отвечающий за отображение данных
        return super(UserTemplateView, self).dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User  # передаем данному классу таблицу(model) со списком пользователей
    template_name = 'admins/admin-users.html'  # указываем где нужно отоброжать объекты (User)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):  # метод, отвечающий за отображение данных
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.get_success_url())

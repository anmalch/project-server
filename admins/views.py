from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)  # возвращается генерация шаблона


# CRUD: Read
def admin_users(request):
    context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users.html', context)


# CRUD: Create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))

    else:
        form = UserAdminRegistrationForm()  # Get запрос
    context = {'title': 'GeekShop - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# CRUD: Update
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES,
                                    data=request.POST)  # instance: чтобы форма понимала для какого user мы будем обновлять данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'GeekShop - Редактирование пользователя',
        'selected_user': selected_user,
        'form': form,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# CRUD: Delete

def admin_users_delete(request, id):
    user = User.objects.get(id=id)  # выбираем польз-ля по id из БД
    # user.is_active = False вместо удаления
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))  # перенаправляем на главную страницу

from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket


# конролер авторизации
def login(request):
    # логика авторизации, если POST-запрос
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # создание объекта формы с данными, кот пришли от клиента
        if form.is_valid():
            username = request.POST[
                'username']  # request.POST-Query Dict (джанговский тип данных, неизменяемый словарь)
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)  # проверяем есть ли в БД такой логин с паролем
            if user and user.is_active:  # если такой пользователь есть в системе и активен
                auth.login(request, user)  # тогда мы его авторизуем
                return HttpResponseRedirect(reverse('index'))  # если авторизация прошла успешна, то возвращаем
                # его на страницу index

    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()  # Get запрос
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES,
                               data=request.POST)  # instance: чтобы форма понимала для какого user мы будем обновлять данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    form = UserProfileForm(instance=user)
    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        'baskets': Basket.objects.filter(user=user)}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

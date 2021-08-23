from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm


# конролер авторизации
def login(request):
    # логика авторизации, если POST-запрос
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # создание объекта формы с данными, кот пришли от клиента
        if form.is_valid():
            username = request.POST['username']  # request.POST-Query Dict (джанговский тип данных, неизменяемый словарь)
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)  # проверяем есть ли в БД такой логин с паролем
            if user and user.is_active:  # если такой пользователь есть в системе и активен
                auth.login(request, user)  # тогда мы его авторизуем
                return HttpResponseRedirect(reverse('index'))  # если авторизация прошла успешна, то возвращаем
                # его на страницу index
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'GeekShop - Регистрация'}
    return render(request, 'users/registration.html', context)

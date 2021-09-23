from django.conf import settings
from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from common.views import CommonContextMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileEditForm
from users.models import User
from baskets.models import Basket


class UserLoginView(CommonContextMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Авторизация'


class UserRegistrationView(CommonContextMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    title = 'GeekShop - Регистрация'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_mail(user):
                messages.success(request, 'Сообщение подтверждения отправлено')
                return redirect(self.success_url)
            else:
                messages.success(request, 'Ошибка отправки сообщения')
            return redirect(self.success_url)

    def send_verify_mail(self, user):
        verify_link = reverse('users:verify', args=[user.email, user.activation_key])
        title = f'Подтвержение учетной записи {user.username}'
        message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME}' \
                  f' пройдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

        return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expired():
                user.is_active = True
                user.save()
                auth.login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(self, 'users/verification.html')
            else:
                print(f'error activation user: {user}')
                return render(self, 'users/verification.html')
        except Exception as err:
            print(f'error activation user: {err.args}')
            return HttpResponseRedirect(reverse('index'))


# class UserProfileView(CommonContextMixin, UpdateView):
#    model = User
#    form_class = UserProfileForm
#    template_name = 'users/profile.html'
#    title = 'GeekShop - Личный кабинет'
#
#    def get_success_url(self):
#        return reverse_lazy('users:profile', args=(self.object.id,))
#
#    def get_context_data(self, **kwargs):
#        context = super(UserProfileView, self).get_context_data(**kwargs)
# context['baskets'] = Basket.objects.filter(user=self.object)
#        return context

@transaction.atomic
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(data=request.POST, instance=request.user.shopuserprofile)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'form': form,
        'profile_form': profile_form,
        'title': 'GeekShop - Профиль',
        'baskets': Basket.objects.filter(user=request.user), }

    return render(request, 'users/profile.html', context)


class UserLogoutView(LogoutView):
    pass

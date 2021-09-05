from users.forms import UserRegistrationForm
from django import forms
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:  # объявляем класс Мета, чтобы указать доп. поле с изображением
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')

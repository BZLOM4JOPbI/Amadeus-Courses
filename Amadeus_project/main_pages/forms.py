from .models import *
from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError
from .services import check_username_chars, check_password_correct

class CustomUserForm(ModelForm):

    class Meta:

        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password',]
        widgets = {
            'username': TextInput(attrs={
                'type': "text",  'placeholder': "login"
            }),
            'email': TextInput(attrs={
                'type': "email",  'placeholder': "email"
            }),
            'confirm_password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            }),
            'password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            }),
        }

    # Проверка почты на валидность
    def clean_email(self):
        # почта не зависит от регистра
        email = self.cleaned_data['email'].lower().strip()
        if CustomUser.objects.filter(email__icontains=email).exists():
            raise ValidationError('Это почта уже используется!')
        return email
    
    # Проверка имени на валидность
    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise ValidationError('Это имя уже используется!')
        check_username_chars(username=username)
        return username

    # Проверка пароля на валидность
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password'].strip()
        password = self.cleaned_data['password'].strip()
        check_password_correct(password, confirm_password)
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': '********'}))

from .models import CustomUser
from django.forms import ModelForm, TextInput
from django import forms


class CustomUserForm(ModelForm):

    class Meta:

        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': TextInput(attrs={
                'type': "text",  'placeholder': "login"
            }),
            'email': TextInput(attrs={
                'type': "email",  'placeholder': "email"
            }),
            'password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            }),
            'confirm_password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            })
        }

    # def clean_email(self):
    #     email = self.cleaned_data['email'].strip()
    #     if CustomUser.objects.filter(email__iexact=email).exists():
    #         raise SyntaxError('Это почта уже используется!')
    #     return email

    # def clean_username(self):
    #     username = self.cleaned_data['username'].strip()
    #     if CustomUser.objects.filter(username__iexact=username).exists():
    #         raise ValidationError('Это имя уже используется!')
    #     return username

    # def clean(self):
    #     confirm_password = self.cleaned_data['confirm_password'].strip()
    #     password = self.cleaned_data['password'].strip()
    #     if password != confirm_password:
    #         raise SyntaxError('Это не тот пароль!')
    #     if len(password) < 12:
    #         raise SyntaxError('Слишком мал!')
    #     return password, confirm_password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from .models import CustomUser
from django.forms import ModelForm, TextInput


class CustomUserForm(ModelForm):

    class Meta:

        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': TextInput(attrs={
                'type': "text",  'placeholder': "login", 'class': 'test'
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




# class CustomUserCreationForm(UserCreationForm):

#     class Meta:

#         model = CustomUser
#         fields = ['username', 'email']


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:

#         model = CustomUser
#         fields = ['username', 'email']

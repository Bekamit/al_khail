from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter password', 'type': 'password'}, ),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter password', 'type': 'password'}, ),
        }

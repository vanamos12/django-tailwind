from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2'] 
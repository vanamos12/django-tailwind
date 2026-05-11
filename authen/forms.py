from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    role = forms.ChoiceField(choices=[('client', 'Client'), ('seller', 'Seller')], required=True)
    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'phone', 'password1', 'password2'] 
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    role = forms.ChoiceField(choices=[('client', 'Client'), ('seller', 'Seller')], required=True)
    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'phone', 'password1', 'password2'] 
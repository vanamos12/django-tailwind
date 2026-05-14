from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2','role'] 

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un compte existe deja avec cet email.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip().replace(' ', '')
        if not phone.startswith('+221'):
            raise forms.ValidationError("Le numero doit commencer par +221.")
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Un compte existe deja avec ce numero.")
        return phone


class OTPVerificationForm(forms.Form):
    code = forms.CharField(
        label="Code OTP",
        min_length=6,
        max_length=6,
        widget=forms.TextInput(attrs={'autocomplete': 'one-time-code'})
    )


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label="Email ou nom d'utilisateur"
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:

            if "@" in username:
                try:
                    user_obj = User.objects.get(email=username)
                    username = user_obj.username
                except User.DoesNotExist:
                    raise forms.ValidationError(
                        "Email ou mot de passe incorrect."
                    )

            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Email ou mot de passe incorrect."
                )

        return self.cleaned_data
    

from django.urls import path
from .forms import AuthForm
from .views import registerViews, verifyOTPViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',loginViews , name='login' ),
    path('', auth_views.LoginView.as_view(authentication_form=AuthForm), name='login' ),
    path('register/', registerViews, name='register'),
    path('verify-otp/', verifyOTPViews, name='verify_otp'),
    # path('', home , name='home')
]

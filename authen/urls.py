from django.urls import path
from .views import registerViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',loginViews , name='login' ),
    path('', auth_views.LoginView.as_view(), name='login' ),
    path('register/', registerViews, name='register'),
    # path('', home , name='home')
]

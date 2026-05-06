from django.urls import path
from .views import registerViews
from django.contrib.auth import views as auth_views,logoutView

urlpatterns = [
    
    path('login',loginViews , name='login' ),
    path('register', registerViews, name='register'),
    path('', home , name='home'),
    path('logout',logoutView, name='logout')
    
]

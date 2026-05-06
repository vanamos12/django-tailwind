from django.urls import path
from .views import loginViews, registerViews,home,logoutView

urlpatterns = [
    
    path('login',loginViews , name='login' ),
    path('register', registerViews, name='register'),
    path('', home , name='home'),
    path('logout',logoutView, name='logout')
    
]

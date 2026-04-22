from django.urls import path
from .views import loginViews, registerViews,home

urlpatterns = [
    
    path('login/',loginViews , name='login' ),
    path('register/', registerViews, name='register'),
    path('', home , name='home')
]

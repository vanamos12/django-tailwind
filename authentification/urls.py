from django.urls import path
from django.contrib.auth import login
from .views import connexion

urlpatterns = [
    path('', connexion, name='login'),
]

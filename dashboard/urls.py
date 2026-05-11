from django.urls import path,include
from .views import dashboard_client
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_client),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
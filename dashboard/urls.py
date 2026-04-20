from django.urls import path,include
from .views import dashboard_client
urlpatterns = [
    path('', dashboard_client),
]

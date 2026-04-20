from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, 'authen/index.html')
def loginViews(request):
    return render(request, 'authen/login.html')

def registerViews(request):
    return render(request, 'authen/register.html')

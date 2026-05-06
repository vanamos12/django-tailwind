from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm



# Create your views here.

# def home(request):
#     return render(request, 'authen/index.html')
# def loginViews(request):
#     return render(request, 'authen/login.html')

User= get_user_model()
def registerViews(request):
    print('register')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form':form})
    return render(request, 'registration/register.html', {'form':form}) 
from django.shortcuts import render

def index(request):
	age:int = 30
	sum = 23 + 45
	return render(request, 'index.html', {'age': age, 'sum': sum})

def login(request):
	print(request.POST.get('username', 'not yet'))
	print(request.POST.get('password', 'not yet'))
	return render(request, 'login.html', {})

def register(request):
	return render(request, 'register.html', {})
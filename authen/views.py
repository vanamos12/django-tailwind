from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.
error=None
def home(request):
    return render(request, 'authen/index.html')
def loginViews(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        user= authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            send_mail(
                subject='Connexion a votre compte !',
                message= f"Bonjour {user} \nNous vous informons qu'une connexion a été effectuée avec succès",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list= [email],
                fail_silently=False,
            )
            return redirect('d_client')

        else:
            messages.error(request, "Email ou mot de passe incorrect !")
            return redirect('login')
    return render(request, 'authen/login.html')

User= get_user_model()
def registerViews(request):
    
    if request.method=='POST':
        email = request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm-password']
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "L'Email invalide")
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, "Les mot de passe ne sont pas identique")
            return redirect('register')
       
        try:
            user= User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
        except IntegrityError:
            messages.error(request, f"Email {email} est deja utiliser !")
            return redirect('register')
        
        send_mail(
            subject="Bienvenue dans notre site ",
            message=f"Bonjour {email}, votre compte a ete creer avec succes",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        messages.success(request, "Compte creer avec sucess !")
        return redirect('d_client')
        
        
    return render(request, 'authen/register.html')
def logoutView(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    

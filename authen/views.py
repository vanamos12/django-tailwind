from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from .forms import OTPVerificationForm, RegisterForm, AuthForm
from .sms import create_phone_otp, send_registration_otp, verify_phone_otp

User = get_user_model()


def home(request):
    return render(request, 'authen/index.html')


def loginViews(request):

    form = AuthForm()

    if request.method == 'POST':

        form = AuthForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    return render(request, 'authen/login.html', {'form': form})


def registerViews(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            otp, code = create_phone_otp(user)

            try:
                send_registration_otp(user, code)
            except Exception as exc:
                otp.delete()
                user.delete()
                error_message = "Impossible d'envoyer le SMS OTP. Verifiez la configuration IntechSMS."
                if settings.DEBUG:
                    error_message = f"{error_message} Detail: {exc}"
                form.add_error(None, error_message)
            else:
                request.session['pending_otp_user_id'] = user.id
                messages.success(request, "Un code OTP a ete envoye par SMS.")
                return redirect('verify_otp')

    return render(request, 'registration/register.html', {'form': form})


def verifyOTPViews(request):
    user_id = request.session.get('pending_otp_user_id')
    if not user_id:
        messages.error(request, "Veuillez commencer par l'inscription.")
        return redirect('register')

    try:
        user = User.objects.get(id=user_id, is_active=False)
    except User.DoesNotExist:
        request.session.pop('pending_otp_user_id', None)
        return redirect('login')

    form = OTPVerificationForm()
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            if verify_phone_otp(user, form.cleaned_data['code']):
                request.session.pop('pending_otp_user_id', None)
                messages.success(request, "Compte verifie. Vous pouvez vous connecter.")
                return redirect('login')
            form.add_error('code', "Code OTP invalide ou expire.")

    return render(request, 'registration/verify_otp.html', {'form': form, 'phone': user.phone})

import json
import secrets
from datetime import timedelta

import requests
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone

from .models import PhoneOTP


class SMSSendError(Exception):
    pass


def generate_otp_code():
    return f"{secrets.randbelow(1000000):06d}"


def create_phone_otp(user):
    code = generate_otp_code()
    otp = PhoneOTP.objects.create(
        user=user,
        code_hash=make_password(code),
        expires_at=timezone.now() + timedelta(minutes=settings.OTP_EXPIRE_MINUTES),
    )
    return otp, code


def verify_phone_otp(user, code):
    otp = user.phone_otps.filter(verified_at__isnull=True).first()
    if otp is None or otp.is_expired:
        return False
    if not check_password(code, otp.code_hash):
        return False

    otp.verified_at = timezone.now()
    otp.save(update_fields=['verified_at'])
    user.is_active = True
    user.save(update_fields=['is_active'])
    return True


def send_sms(msisdn, content):
    if not settings.INTECHSMS_APP_KEY:
        raise ImproperlyConfigured("INTECHSMS_APP_KEY est manquant dans le fichier .env.")

    payload = {
        "app_key": settings.INTECHSMS_APP_KEY,
        "sender": settings.INTECHSMS_SENDER,
        "content": content,
        "msisdn": [msisdn],
    }
    try:
        response = requests.post(
            settings.INTECHSMS_URL,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=15,
        )
    except requests.RequestException as exc:
        raise SMSSendError(f"Erreur reseau IntechSMS: {exc}") from exc

    if not response.ok:
        raise SMSSendError(f"IntechSMS HTTP {response.status_code}: {response.text[:300]}")

    response_text = response.text.strip()
    if response_text:
        try:
            response_data = response.json()
        except ValueError:
            response_data = None

        if isinstance(response_data, dict):
            if response_data.get("error") is True:
                raise SMSSendError(f"IntechSMS a refuse le SMS: {response_text[:300]}")
        elif any(word in response_text.lower() for word in ["invalid", "failed", "unauthorized"]):
            raise SMSSendError(f"IntechSMS a refuse le SMS: {response_text[:300]}")

    return response


def send_registration_otp(user, code):
    message = f"Votre code de verification est {code}. Il expire dans {settings.OTP_EXPIRE_MINUTES} minutes."
    return send_sms(user.phone, message)

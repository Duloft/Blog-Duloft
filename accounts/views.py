from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.conf import settings

def login(request):
    sso_login_url = f"{settings.SSO['ROOT']}/user/login/?next={request.build_absolute_uri('/')}"
    return redirect(sso_login_url)


def logout(request):
    sso_logout_url = f"{settings.SSO['ROOT']}/user/logout/"
    return redirect(sso_logout_url)

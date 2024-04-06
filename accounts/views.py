
# Create your views here.

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

def login(request):
    next_url = request.GET.get('next')
    sso_login_url = f"{settings.SSO['ROOT']}/user/login/?next={redirect(next_url)}"
    return redirect(sso_login_url)


def logout(request):
    sso_logout_url = f"{settings.SSO['ROOT']}/user/logout/"
    return redirect(sso_logout_url)

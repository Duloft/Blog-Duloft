
# Create your views here.

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

def login(request):
    sso_login_url = f"{settings.SSO['ROOT']}/user/login/?next={reverse('blog_post')}"
    return redirect(sso_login_url)


def logout(request):
    sso_logout_url = f"{settings.SSO['ROOT']}/user/logout/"
    return redirect(sso_logout_url)

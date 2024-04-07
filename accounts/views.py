
# Create your views here.

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

def login(request):
    # Construct the login URL for the SSO server
    login_url = f"{settings.SOS['ROOT']}/sso/login/?next={reverse('blog_post')}"

    # Redirect the user to the SSO server for authentication
    return redirect(login_url)


def logout(request):
    sso_logout_url = f"{settings.SSO['ROOT']}/sos/logout/"
    return redirect(sso_logout_url)

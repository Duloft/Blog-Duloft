from django.utils.text import slugify

from . import models

import string
import random


def generate_random_string(Num):
    res = "-".join(random.choices(string.ascii_uppercase + string.digits, k = Num))
    return res


def generate_slug(text):
    
    gen_slug = slugify(text)
    
    # if models.PostModel.objects.filter(slug = gen_slug).exists():
    #     gen_slug = gen_slug + generate_random_string(5)
        
    return gen_slug



import requests
from django.conf import settings

def check_auth_status(access_token):
    domain = '127.0.0.1:8000' if settings.DEBUG else 'app.duloft.com'

    
    url = f'http://{domain}/auth/api/auth-status/'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.json().get('authenticated', False):
        return True, response.json()
    return False, None

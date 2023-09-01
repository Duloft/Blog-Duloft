# waitlist/models.py
from django.db import models

class Waitlist(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    own_a_house = models.BooleanField(default=False)
    manage_my_property = models.BooleanField(default=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

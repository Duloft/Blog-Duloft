from django.contrib import admin
from .models import Waitlist
# Register your models here.

class WaitlistAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'email',
        'state','location',
        'own_a_house',
        'manage_my_property'
        ]
    
    search_fields = [
        'full_name',
        'phone_number',
        'state',
    ]
    list_per_page = 10
    
admin.site.register(Waitlist, WaitlistAdmin)


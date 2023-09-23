from django.contrib import admin
from .models import Complaint

# Register your models here.

class ComplaintAdmin(admin.ModelAdmin):
    list_display = [
        'sender_number',
        'message',
        'done',
        'timestamp', 
        ]
    
    list_per_page = 10
   

admin.site.register(Complaint, ComplaintAdmin)
from django.contrib import admin
from .models import CustomerLog

# Register your models here.

class CustomerLogAdmin(admin.ModelAdmin):
    list_display = [
        'customer_name',
        'status',
        'date_updated',
        'date_filed', 
        ]
    
    search_fields = [
        'customer_name',
        'status',
        'date_filed', 
    ]
    list_per_page = 10
   

admin.site.register(CustomerLog, CustomerLogAdmin)

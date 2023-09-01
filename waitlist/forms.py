from django import forms
from .models import Waitlist


class WaitListForm(forms.ModelForm):
    
    class Meta:
        model = Waitlist
        fields = "__all__"
        
        
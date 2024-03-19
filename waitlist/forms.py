from django import forms
from .models import Waitlist
from django_recaptcha.fields import ReCaptchaField


class WaitListForm(forms.ModelForm):
    own_a_house = forms.BooleanField(required=False, label="I own a house and I want to rent or sell", 
                                    widget=forms.CheckboxInput(attrs={'class':'form-control-check-input'}))
    
    manage_my_property = forms.BooleanField(label="I want DuLoft to manage my property", required=False, 
                                    widget=forms.CheckboxInput(attrs={'class':'form-control-check-input'}))
    
    captcha = ReCaptchaField()
    class Meta:
        model = Waitlist
        fields = "__all__"
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'The area in your state where you live.'})
        }
        
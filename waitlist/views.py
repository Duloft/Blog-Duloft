# waitlist/views.py
from django.shortcuts import render, redirect
# from .models import Waitlist
from .forms import WaitListForm

def join_waitlist(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('waitlist_success')
            
    else:
        form = WaitListForm()    
    
        return render(request, 'waitlist/join_waitlist.html', {'form':form})

def waitlist_success(request):
    return render(request, 'waitlist/waitlist_success.html')

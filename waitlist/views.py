# waitlist/views.py
from django.shortcuts import render, redirect
# from .models import Waitlist
from honeypot.decorators import check_honeypot
from .forms import WaitListForm

@check_honeypot
def join_waitlist(request):
    form = WaitListForm()    
    if request.method == 'POST':
        form = WaitListForm(request.POST)
        # print('here......')
        if form.is_valid():
            # print('valid...')
            # print("form Data")
            # print(form.changed_data['full_name'])
            # print(form.changed_data['phone_number'])
            # print(form.changed_data['email'])
            # print(form.changed_data['state'])
            form.save()
            return redirect('waitlist_success')
    
    
    return render(request, 'waitlist/join_waitlist.html', {'form':form})

def waitlist_success(request):
    return render(request, 'waitlist/waitlist_success.html')

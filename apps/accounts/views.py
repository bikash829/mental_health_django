from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ChangeProfilePhoto
from pprint import pprint
from django.contrib import messages
# Create your views here.
@login_required
def profile(request):
    template_name = "patient/profile.html"
    context  = {

    }
    
    return render(request,template_name,context)

def change_profile_photo(request):
    if request.method == "POST":
        form = ChangeProfilePhoto(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            error_messages = "\n".join([error for errors in form.errors.values() for error in errors])
            messages.error(request,error_messages)
        return redirect('accounts:profile')

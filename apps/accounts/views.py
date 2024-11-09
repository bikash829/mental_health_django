from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ChangeProfilePhoto
from pprint import pprint
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm


# Create your views here.
@login_required
def profile(request):
    template_name = "patient/profile.html"
    context  = {

    }
    
    return render(request,template_name,context)

@login_required
def change_profile_photo(request):
    if request.method == "POST":
        form = ChangeProfilePhoto(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            error_messages = "\n".join([error for errors in form.errors.values() for error in errors])
            messages.error(request,error_messages)
        return redirect('accounts:profile')



def user_registration(request):
    form = UserRegistrationForm

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('accounts:login')
            print(form.cleaned_data)
        else:
            error_messages = "\n".join([error for errors in form.errors.values() for error in errors])
            messages.error(request,error_messages)

    template_name = "registration/register.html"
    context = {
        'form': form,
    }
    pprint(form)
    return render(request,template_name,context)
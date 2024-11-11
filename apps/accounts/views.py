from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ChangeProfilePhoto
from pprint import pprint
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group


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
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data.get('role')
            
            try: 
                group = Group.objects.get(name=role)
                user.save()
                user.groups.add(group)
                messages.success(request,"Your account has been registered successfully")
                return redirect('accounts:login')
            except Group.DoesNotExist:
                messages.error(request, f"The role '{role}' does not exist.")
        # else:
        #     error_messages = "\n".join([error for errors in form.errors.values() for error in errors])
        #     messages.error(request,error_messages)
    
    template_name = "registration/register.html"
    context = {
        'form': form,
    }
    # Print the properties of the 'role' field
    role_field = form['role']
    for role in role_field:
        # pprint(vars(role))
        print(role.data['label'])

    return render(request,template_name,context)
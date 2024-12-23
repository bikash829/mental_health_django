from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ChangeProfilePhoto
from pprint import pprint
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
# email verification's utilities
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


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
            user.is_active = False
            user.is_verified = 2
            role = form.cleaned_data.get('role')
            
            try: 
                group = Group.objects.get(name=role)
                user.save()
                user.groups.add(group)
                 # Send email verification
                current_site = get_current_site(request)
                subject = 'Activate Your Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                send_mail(subject, message, 'from@example.com', [user.email])
                return redirect('accounts:account_activation_sent')
            
                # messages.success(request,"Your account has been registered successfully")
                # return redirect('accounts:login')
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



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # user = User.objects.get(pk=uid)
        user = get_object_or_404(User, pk=uid)
    # except (TypeError, ValueError, OverflowError, User.DoesNotExist):
    except (TypeError, ValueError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.save()
        messages.success(request,"Your account has been verified")
        return redirect('accounts:login')
    else:
        # return render(request, 'accounts/account_activation_invalid.html')
        return HttpResponse('Invalid response')
    


def account_activation_sent(request):
    template_name = "account_activation_sent.html"
    context = {

    }

    return render(request,template_name,context)
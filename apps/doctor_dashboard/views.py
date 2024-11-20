from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test,login_required

def group_required(*group_names,login_url='accounts:login'):
    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name__in=group_names).exists():
                return True
            
        return False
    return user_passes_test(in_groups,login_url=login_url)


# Create your views here.
@login_required
@group_required('doctor',login_url='accounts:login')
def index(request):
    template_name = "doctor/dashboard.html"
    context={

    }
    return render(request,template_name,context)


@login_required
@group_required('doctor',login_url='accounts:login')
def profile_update(request):
    form = None 

    template_name = "doctor/manage_profile/wiz_form.html"
    context = {
        'form': form,
    }
    return render(request,template_name,context)

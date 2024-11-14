from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test,login_required

def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name__in=group_names).exists():
                return True
            
        return False
    return user_passes_test(in_groups)


# Create your views here.
@login_required
def index(request):
    template_name = "dashboard/layouts/base.html"
    context={

    }
    return render(request,template_name,context)

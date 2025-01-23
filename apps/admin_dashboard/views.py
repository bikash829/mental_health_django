from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q
User =  get_user_model()

# Create your views here.s
def index(request):
    
    template_name = "admin_dashboard/dashboard.html"
    context={

    }
    return render(request,template_name,context)

def is_superuser(user):
    return user.is_superuser

@method_decorator(user_passes_test(is_superuser), name='dispatch')
class PendingUserListView(ListView):
    model = User
    queryset = User.objects.filter(
        (Q(groups__name='doctor') | Q(groups__name='counselor')) & Q(is_verified=3)
    )
    # context_object_name = "users"
    
    template_name = "admin_dashboard/manage_users/pending_users.html"


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class ShowUserProfileDetails(DetailView):
    model = User
    context_object_name = 'user_details'
    template_name = "admin_dashboard/manage_users/user_profile.html"

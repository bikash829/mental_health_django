from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    template_name = "accounts/patient/profile.html"
    context  = {

    }
    return render(request,template_name,context)

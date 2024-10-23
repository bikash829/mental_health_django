from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BasicInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pprint
# Create your views here.

@login_required
def edit_basic_info(request):
    form = BasicInfoForm(instance=request.user)
    if request.method == 'POST':
        form = BasicInfoForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"You profile basic info has been updated")
            return redirect('accounts:profile')
    template_name = 'patient/manage_profile/basic_info.html'
    pprint.pprint(form)
    context = {
        'form': form,
    }
    return render(request,template_name,context)


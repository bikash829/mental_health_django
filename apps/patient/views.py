from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pprint import pprint
from .forms import BasicInfoForm,AddressForm,PatientContactForm
from mental_health.custom_forms_renderer import BootstrapErrorList
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

@login_required
def edit_address(request):
    # form = AddressForm(instance=request.user.address,error_class=BootstrapErrorList)
    form = AddressForm(instance=request.user.address)
    if request.method == "POST":
        form = AddressForm(request.POST,instance=request.user.address)
        if form.is_valid():
            form.save()
            messages.success(request,"You address has been updated")
            return redirect('accounts:profile')
    template_name = 'patient/manage_profile/edit_address.html'
    # rendered_form = form.render("custom_form_template/form_snippet.html")
    context = {
        'form': form,
    } 
    return render(request,template_name,context)


@login_required
def edit_contact(request):
    if request.method == "POST":
        form = PatientContactForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact number has been updated")
            return redirect('accounts:profile')
    else:
        form = PatientContactForm(instance=request.user)  # Prepopulate form with existing data

   
    # pprint(form)
    template_name = 'patient/manage_profile/edit_contact_info.html'
    context = {
        'form': form,
    } 


    return render(request,template_name,context)

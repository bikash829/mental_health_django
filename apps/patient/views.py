from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pprint import pprint

from apps.accounts.models import Address
from apps.patient.models import BiologicalInfo, BloodSugar, VitalSignsReport
from .forms import AddBiologicalInfoForm, BasicInfoForm,AddressForm,PatientContactForm,AddBloodSugarInfo,AddVitalSignInfo,UpdateBiologicalInfo
from mental_health.custom_forms_renderer import BootstrapErrorList
# Create your views here.
@login_required
def profile(request):
    template_name = "patient/profile.html"
    context  = {

    }
    
    return render(request,template_name,context)


@login_required
def edit_basic_info(request):
    form = BasicInfoForm(instance=request.user)
    if request.method == 'POST':
        form = BasicInfoForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"You profile basic info has been updated")
            return redirect('patient:profile')
    template_name = 'patient/manage_profile/basic_info.html'
    context = {
        'form': form,
    }
    return render(request,template_name,context)


@login_required
def edit_address(request):
    # form = AddressForm(instance=request.user.address,error_class=BootstrapErrorList)
    if not hasattr(request.user, 'address'):
        Address.objects.create(user=request.user)
    form = AddressForm(instance=request.user.address)
    if request.method == "POST":
        form = AddressForm(request.POST,instance=request.user.address)
        if form.is_valid():
            form.save()
            messages.success(request,"You address has been updated")
            return redirect('patient:profile')
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
            print(form.cleaned_data['additional_phone'])
            additional_phone = form.cleaned_data.get('additional_phone')
            # if isinstance(additional_phone, list):
            #     print('checked list or not')
            #     if not additional_phone:  # Check if the list is empty
            #         form.cleaned_data['additional_phone'] = ""
            #         print('assigned empty value')
            additional_phone = form.cleaned_data.get('additional_phone')
            if isinstance(additional_phone, list) and not additional_phone:  # Check if the list is empty
                form.cleaned_data['additional_phone'] = None
            print(form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Your contact number has been updated")
            return redirect('patient:profile')
    else:
        form = PatientContactForm(instance=request.user)  # Prepopulate form with existing data

   
    # pprint(form)
    template_name = 'patient/manage_profile/edit_contact_info.html'
    context = {
        'form': form,
    } 

    return render(request,template_name,context)


@login_required
def add_vital_sign_info(request):
    form = AddVitalSignInfo()
    if request.method == "POST":
        form = AddVitalSignInfo(request.POST)
        if form.is_valid():
            vital_sign  = form.save(commit=False)
            vital_sign.user = request.user
            vital_sign.save()
            messages.success(request, "Your vital sings report has been updated")
            return redirect('patient:profile') 

    template_name = "patient/manage_profile/vital_sign_form.html" 
    context = {
        'form' : form,
    }
    return render(request,template_name,context)


@login_required
def delete_vital_sign_report(request,id):
    data = VitalSignsReport.objects.get(pk=id)
    data.delete()
    messages.success(request, "Your vital sings report has been deleted")
    return redirect('patient:profile') 


@login_required
def add_blood_sugar_info(request):
    form = AddBloodSugarInfo

    if request.method == "POST":
        form = AddBloodSugarInfo(request.POST)
        if form.is_valid():
            blood_sugar = form.save(commit=False)
            blood_sugar.user = request.user
            blood_sugar.save()

            messages.success(request, "Your blood sugar report has been updated")
            return redirect('patient:profile') 
    template_name = "patient/manage_profile/blood_sugar_form.html" 
    context = {
        'form' : form 
    }
    return render(request,template_name,context) 


@login_required
def delete_blood_sugar_report(request,id):
    report = BloodSugar.objects.get(id=id)
    report.delete()
    messages.info(request, "Your blood sugar report has been deleted")
    return redirect('patient:profile') 


@login_required
def update_biological_info(request,id):
    data = BiologicalInfo.objects.get(pk=id)
    form = UpdateBiologicalInfo(instance=data)

    if request.method == "POST":
        form = UpdateBiologicalInfo(request.POST,instance=data)
        if form.is_valid():
            bio_info = form.save(commit=False)
            bio_info.user = request.user
            bio_info.save()
            messages.success(request, "Your personal info has been updated")
            return redirect('patient:profile') 
    template_name = "patient/manage_profile/biological_info_form.html" 
    context = {
        'form': form
    }
    return render(request,template_name,context) 


@login_required
def add_biological_info(request):
    form = AddBiologicalInfoForm()
    if request.method == "POST":
        form = AddBiologicalInfoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Your personal info has been updated")
            return redirect('patient:profile') 
    template_name = "patient/manage_profile/biological_info_form.html" 
    context = {
        'form': form,
        'banner_title': 'Add Info',
    }
    return render(request,template_name,context) 
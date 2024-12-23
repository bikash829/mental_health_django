from django.shortcuts import render

from apps.accounts.models import Address
from apps.doctor_dashboard.models import Expert
from .forms import AddressForm, UpdateDoctorProfile,ExpertForm

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
    if not hasattr(request.user, 'expert'):
        Expert.objects.create(user=request.user)
    if not hasattr(request.user, 'address'):
        Address.objects.create(user=request.user)

    form = UpdateDoctorProfile(instance=request.user) 
    expert_info_form = ExpertForm(instance=request.user.expert)
    address_form = AddressForm(instance=request.user.address)

    # pprint.pprint(address_form)
    # pprint.pprint(form)
    # pprint.pprint(expert_info_form)
    # pprint.pprint(form.first_name)
    

    template_name = "doctor/manage_profile/wiz_form.html"
    context = {
        'form': form,
        'form_expert_info': expert_info_form,
        'form_address' : address_form,
    }
    return render(request,template_name,context)

from django.http import JsonResponse
from pprint import pprint 
from django.db import transaction

@login_required
@group_required('doctor',login_url='accounts:login')
def update_initial_info(request):
    pprint(request)
    if request.method == 'POST':
        # Bind both forms with POST data and files
        form = UpdateDoctorProfile(request.POST, request.FILES, instance=request.user)
        expert_info_form = ExpertForm(request.POST, request.FILES, instance=request.user.expert)
        address_form = AddressForm(request.POST, instance=request.user.address)

        # print('general info')
        # pprint.pprint(form)
        # print('expert info')
        # pprint.pprint(expert_info_form)
        # print('address info')
        # pprint.pprint(address_form)
        # pprint.pprint(request.POST)


        if form.is_valid() and expert_info_form.is_valid() and address_form.is_valid(): 
            # print('clean form')
            # pprint.pprint(form.cleaned_data)
            # print('clean expert data')
            # pprint.pprint(expert_info_form.cleaned_data)
            # print('clean address data')
            # pprint.pprint(address_form.cleaned_data)

            with transaction.atomic():
                form.save()  # Save the changes for the first form
                expert_info_form.save()  # Save the changes for the second form
                address_form.save()  # Save the changes for the second form
            return JsonResponse({'message': 'Success'})
        else:
            # Collect errors from both forms
            errors = {**form.errors, **expert_info_form.errors, **address_form.errors}
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
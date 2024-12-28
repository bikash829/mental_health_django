from django.shortcuts import render

from apps.accounts.models import Address, Education, Training
from apps.doctor_dashboard.models import Expert
from .forms import AddressForm, FormEducation, FormTraining, UpdateDoctorProfile,ExpertForm

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
    formEducation = FormEducation()
    form_training = FormTraining()
    # pprint.pprint(address_form)
    # pprint.pprint(form)
    # pprint.pprint(expert_info_form)
    # pprint.pprint(form.first_name)
    

    template_name = "doctor/manage_profile/wiz_form.html"
    context = {
        'form': form,
        'form_expert_info': expert_info_form,
        'form_address' : address_form,
        'formEducation' : formEducation,
        'form_training' : form_training
    }
    return render(request,template_name,context)

from django.http import JsonResponse
from pprint import pprint 
from django.db import transaction

@login_required
@group_required('doctor',login_url='accounts:login')
def update_initial_info(request):
    if request.method == 'POST':
        # Bind both forms with POST data and files
        form = UpdateDoctorProfile(request.POST, request.FILES, instance=request.user)
        expert_info_form = ExpertForm(request.POST, request.FILES, instance=request.user.expert)
        address_form = AddressForm(request.POST, instance=request.user.address)


        if form.is_valid() and expert_info_form.is_valid() and address_form.is_valid(): 
            with transaction.atomic():
                form.save()  # Save the changes for the first form
                expert_info_form.save()  # Save the changes for the second form
                address_form.save()  # Save the changes for the second form
            return JsonResponse({'message': 'You personal information has been updated'})
        else:
            # Collect errors from both forms
            errors = {**form.errors, **expert_info_form.errors, **address_form.errors}
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
from django.db.models import F
from django.core import serializers
@login_required
@group_required('doctor',login_url='accounts:login')
def update_education_info(request):
    if request.method == 'POST':
        # Bind both forms with POST data and files
        formEducation = FormEducation(request.POST, request.FILES)
        if formEducation.is_valid():
            formEducation.save()
            
            # education_set = request.user.education_set.all()
            # education_set = serializers.serialize('json', education_set)

            # django orm 
            education_set = request.user.education_set.select_related('specialization').values(
                'id', 'institute', 'specialization__title', 'duration', 'passing_year', 'certificate','certificate_title'
            )
            educations = list(education_set)
            return JsonResponse({'message': 'Education information has been updated','educations':educations})
        else:
            # Collect errors from both forms
            errors = formEducation.errors
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
@group_required('doctor',login_url='accounts:login')
def delete_education(request):
    if request.method == 'POST':
        education_id = request.POST.get('id')
        try:
            education = Education.objects.get(id=education_id, user=request.user)
            education.delete()
            return JsonResponse({'message': 'Education information has been deleted successfully'})
        except Education.DoesNotExist:
            return JsonResponse({'error': 'Education information not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


# training info
@login_required
@group_required('doctor',login_url='accounts:login')
def update_training(request):
    if request.method == 'POST':
        # Bind both forms with POST data and files
        pprint(request.POST)
        form_training = FormTraining(request.POST, request.FILES)
        if form_training.is_valid():
            form_training.save()

            # django orm 
            training_set = request.user.training_set.select_related('specialization').values(
                'id', 'institute', 'specialization__title', 'from_date', 'to_date', 'training_certificate','training_title'
            )
            trainings = list(training_set)
            return JsonResponse({'message': 'Training information has been updated','trainings':trainings})
        else:
            # Collect errors from both forms
            errors = form_training.errors
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
@group_required('doctor',login_url='accounts:login')
def delete_training(request):
    print("here you are")
    if request.method == 'POST':
        training_id = request.POST.get('id')
        print(training_id)
        try:
            training = Training.objects.get(id=training_id, user=request.user)
            training.delete()
            return JsonResponse({'message': 'Training information has been deleted successfully'})
        except Training.DoesNotExist:
            return JsonResponse({'error': 'Training information not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

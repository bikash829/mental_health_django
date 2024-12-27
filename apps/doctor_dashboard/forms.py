from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User, Education
from apps.doctor_dashboard.models import Expert, Specialization
from apps.accounts.models import Address
from phonenumber_field.formfields import SplitPhoneNumberField, PrefixChoiceField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms import ModelForm
from django.core.validators import RegexValidator, MaxLengthValidator


class UpdateDoctorProfile(UserChangeForm):
    phone = SplitPhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            widgets=[
                forms.Select(attrs={'class': 'form-select w-25'},choices=PrefixChoiceField().choices),
                forms.TextInput(attrs={'class': 'form-control w-75'})
                ],
        )
    )

    additional_phone=SplitPhoneNumberField(
        required=False,  # Make this field optional,
        widget=PhoneNumberPrefixWidget(
            widgets=[
                forms.Select(attrs={'class': 'form-select w-25'},choices=PrefixChoiceField().choices),
                forms.TextInput(attrs={'class': 'form-control w-75'})
                ],
        ),
        
    )


    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'gender', 'date_of_birth', 
            'marital_status', 'nationality', 'phone', 'additional_phone', 
            'identity_type','identity_proof', 'identity_no', 
        ]
    #  'identity_proof',

class ExpertForm(ModelForm):
    class Meta:
        model= Expert
        fields= "__all__"
        # fields = ['doc_title', 'license_no', 'license_attachment_file',]
        exclude = ['user'] 



class AddressForm(ModelForm):
    zip_code = forms.CharField(
        validators=[
            RegexValidator(regex='^[0-9]*$', message='Zip code must contain only digits from 0-9'),
            MaxLengthValidator(8, message='Zip code must be at most 8 digits long')
        ]
    )

    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['user'] 

SPECIALIZATIONS_CHOICES = [
    "Clinical Psychology",
    "Counseling Psychology",
    "School Psychology",
    "Industrial-Organizational Psychology",
    "Health Psychology",
    "Forensic Psychology",
    "Sports Psychology",
    "Neuropsychology",
    "Social Psychology",
    "Developmental Psychology",
    "Experimental Psychology",
    "Cognitive Psychology",
    "Positive Psychology",
    "Environmental Psychology",
    "Consumer Psychology",
    "Others"
    ]

class FormEducation(ModelForm):
    specialization = forms.ModelChoiceField(
        queryset=Specialization.objects.all(),
        empty_label="Select Specialization",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Education
        fields="__all__"
        # exclude = ['user']
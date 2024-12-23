from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User
from apps.doctor_dashboard.models import Expert
from apps.accounts.models import Address
from phonenumber_field.formfields import SplitPhoneNumberField, PrefixChoiceField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms import ModelForm


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
            'identity_type', 'identity_no', 
        ]
    #  'identity_proof',

class ExpertForm(ModelForm):
    class Meta:
        model= Expert
        fields= "__all__"
        # fields = ['doc_title', 'license_no', 'license_attachment_file',]
        exclude = ['user','license_attachment'] 



class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['user'] 
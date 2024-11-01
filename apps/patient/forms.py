from django import forms
from django.forms import ModelForm
from apps.accounts.models import User,Address
# from mental_health.custom_forms_renderer import CustomFormRenderer
# from apps.main.utils import get_country_codes
from phonenumber_field.formfields import PhoneNumberField,SplitPhoneNumberField, PrefixChoiceField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class BasicInfoForm(ModelForm):
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','date_of_birth','gender','blood_group','religion','nationality']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})  # Use RadioSelect widget for the gender field
        }


class AddressForm(ModelForm):
    template_name = "patient/custom_form/form_snippet.html"
    class Meta:
        model = Address
        exclude = ['user'] 


class PatientContactForm(ModelForm):
    template_name = "patient/custom_form/contact_form_snippet.html"
    phone = SplitPhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            widgets=[
                forms.Select(attrs={'class': 'form-select w-25'},choices=PrefixChoiceField().choices),
                forms.TextInput(attrs={'class': 'form-control w-75'})
                ],
        )
    )

    # additional_phone = PhoneNumberField(
    #     widget=forms.TextInput(attrs={'class':'form-control'})
    # )
    additional_phone=SplitPhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            widgets=[
                forms.Select(attrs={'class': 'form-select w-25'},choices=PrefixChoiceField().choices),
                forms.TextInput(attrs={'class': 'form-control w-75'})
                ],
        )
    )
    class Meta:
        model = User
        fields = ['email','phone','additional_phone']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }







    
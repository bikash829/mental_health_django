from django import forms
from django.forms import ModelForm
from apps.accounts.models import User,Address
from .models import VitalSignsReport,BloodSugar,BiologicalInfo
# from mental_health.custom_forms_renderer import CustomFormRenderer
# from apps.main.utils import get_country_codes
from phonenumber_field.formfields import PhoneNumberField,SplitPhoneNumberField, PrefixChoiceField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.validators import MinValueValidator, MaxValueValidator


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



class AddVitalSignInfo(ModelForm):
    template_name = "patient/custom_form/custom_field_template.html"
    class Meta:
        model = VitalSignsReport
        fields = '__all__'
        exclude = ['user']
        widgets = {
            # 'systolic': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'diastolic': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'heart_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'checkup_date': forms.DateInput(attrs={'class': 'form-control','type':'date'})
        }

    systolic = forms.IntegerField(
    validators=[MinValueValidator(90), MaxValueValidator(180)],
    widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 20, 'max': 180})
    )
    diastolic = forms.IntegerField(
        validators=[MinValueValidator(60), MaxValueValidator(120)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 40, 'max': 120})
    )
    heart_rate = forms.IntegerField(
        validators=[MinValueValidator(60), MaxValueValidator(120)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 60, 'max': 120})
    )



class AddBloodSugarInfo(ModelForm):
    template_name = "patient/custom_form/custom_field_template.html"
    class Meta:
        model = BloodSugar
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'sugar_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'checkup_date': forms.DateInput(attrs={'class': 'form-control','type':'date'})
        }



class UpdateBiologicalInfo(ModelForm):
    template_name = "patient/custom_form/custom_field_template.html"
    class Meta:
        model = BiologicalInfo
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'})
        }




    
from django import forms
from django.forms import ModelForm
from apps.accounts.models import User,Address
# from mental_health.custom_forms_renderer import CustomFormRenderer
# from apps.main.utils import get_country_codes



PHONE_CODE = get_country_codes().
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
    # phone_code = forms.ChoiceField(choices=get_country_codes(),required=True,)
    # additional_phone_code = forms.ChoiceField(choices=get_country_codes,required=False)
    class Meta:
        model = User
        fields = ['phone_code','phone','additional_phone_code','additional_phone']



    
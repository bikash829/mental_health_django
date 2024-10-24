from django import forms
from django.forms import ModelForm
from accounts.models import User,Address
# from mental_health.custom_forms_renderer import CustomFormRenderer

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
    template_name = "custom_form_template/form_snippet.html"
    class Meta:
        model = Address
        exclude = ['user'] 



    
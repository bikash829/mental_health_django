from django import forms
from django.forms import ModelForm
from accounts.models import User,Address
from mental_health.custom_forms_renderer import CustomFormRenderer

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
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['user'] 


    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.renderer = CustomFormRenderer() # Custom form renderer
        

        for field_name, field in self.fields.items():
            if self[field_name].errors:
                field.widget.attrs.update({'class': 'form-control is-invalid'})
            else:
                field.widget.attrs.update({'class': 'form-control'})   
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from .models import User

class ChangeProfilePhoto(ModelForm):
    # your_name = forms.ImageField(label="Choose Photo",)
    class Meta:
        model = User
        fields = ['profile_photo',]



class UserRegistrationForm(UserCreationForm):
    role = forms.CharField(required=True,error_messages={"required": "You must choose you desired role."})
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','role']


    def clean_role(self):
        data = self.cleaned_data["role"]
        if data not in ['patient','doctor','counselor']:
            raise ValidationError(_("You are trying to pass invalid user role."))

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
        
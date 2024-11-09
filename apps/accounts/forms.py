from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


from .models import User

class ChangeProfilePhoto(ModelForm):
    # your_name = forms.ImageField(label="Choose Photo",)
    class Meta:
        model = User
        fields = ['profile_photo',]



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
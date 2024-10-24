from django import forms
from django.forms import ModelForm


from .models import User

class ChangeProfilePhoto(ModelForm):
    # your_name = forms.ImageField(label="Choose Photo",)
    class Meta:
        model = User
        fields = ['profile_photo',]
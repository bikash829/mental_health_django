from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User,BloodGroup, Education, Address, Training, Experience
# Register your models here.


# admin.site.register(User)
admin.site.register(BloodGroup)

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1

class TrainingInline(admin.StackedInline):
    model = Training
    extra = 1

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    fields = ['username','first_name','last_name','email','password','marital_status','gender','phone_code','phone',
              'additional_phone_code','additional_phone','date_of_birth','religion','identity_type','identity_no','identity_proof',
              'profile_photo','is_verified','blood_group','terms','is_staff']
    
    
    inlines = [
        AddressInline,EducationInline, TrainingInline,ExperienceInline
    ]


# admin.site.register(Group)




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

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

class UserGroupInline(admin.TabularInline):
    model = User.groups.through
    extra = 1

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ["username", "email","gender","date_of_birth","is_verified","get_groups","is_superuser"]

    # fields = ['username','first_name','last_name','email','marital_status','gender','phone_code','phone',
    #           'additional_phone_code','additional_phone','date_of_birth','religion','identity_type','identity_no','identity_proof',
    #           'profile_photo','is_verified','blood_group','terms','is_staff']

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'marital_status', 'gender', 'phone_code', 'phone',
    #                                   'additional_phone_code', 'additional_phone', 'date_of_birth', 'religion', 'identity_type', 'identity_no', 'identity_proof',
    #                                   'profile_photo', 'blood_group', 'terms')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'date_of_birth', 'is_verified', 'is_staff', 'is_active', 'is_superuser', )}
            # 'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'date_of_birth', 'is_verified', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )
    
    
    inlines = [
        AddressInline,EducationInline, TrainingInline,ExperienceInline,UserGroupInline
    ]

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Role'


# admin.site.register(Group)




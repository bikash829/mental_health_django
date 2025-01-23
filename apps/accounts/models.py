from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from pprint import pprint
from phonenumber_field.modelfields import PhoneNumberField

from apps.doctor_dashboard.models import Specialization

# from apps.doctor_dashboard.models import Specialization

def generate_upload_path(instance, filename, base_dir):
    # Extract the file extension
    ext = filename.split('.')[-1]
    # Generate a unique filename using UUID
    unique_filename = f'{uuid.uuid4()}.{ext}'
    # Get the current date
    current_date = datetime.now().strftime('%Y/%m/%d')
    # Construct the upload path
    
    return f'{base_dir}/{instance.username}/{current_date}/{unique_filename}'

def identity_type_directory_path(instance, filename):
    return generate_upload_path(instance, filename, 'identity_type')

def profile_photo_directory_path(instance, filename):
    return generate_upload_path(instance, filename, 'profile')

# education certificate 
def education_certificate_directory_path(instance, filename):
    # instance.username = instance.user.username
    return generate_upload_path(instance.user, filename, 'employee/education_certificates')

# training certificate 
def training_certificate_directory_path(instance, filename):
    # instance.username = instance.user.username
    return generate_upload_path(instance.user, filename, 'employee/training_certificates')

# Create your models here.

# Blood group model
class BloodGroup(models.Model):
    group = models.CharField(max_length=10)


    def __str__(self):
        return self.group

# User model description 
class User(AbstractUser):
    """ choices """
    # marital status
    MARITAL_STATUS = [
        # ("W", "Widow"),
        ("S", "Single"),
        ("IR", "In a Relationship"),
        ("M", "Married"),
        ("D", "Divorced"),
        ("W", "Widow"),
    ]

    # gender 
    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('O', 'others')
    ]

    # identity type 
    class IdentityType(models.IntegerChoices):
        PASSPORT = 1
        NID = 2

    # verification status 
    IS_VERIFIED = [
            (1,"Verified"),
            (2,"Not Verified"),
            (3,"Pending"),
            (4,"Rejected"),
        ]

    email=models.EmailField(unique=True)
    marital_status = models.CharField(max_length=2,choices=MARITAL_STATUS)
    nationality = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER)
    phone = PhoneNumberField()
    additional_phone = PhoneNumberField(blank=True)
    date_of_birth = models.DateField(null=True)
    religion = models.CharField(max_length=50)
    identity_type = models.IntegerField(choices=IdentityType,null=True)
    identity_no = models.CharField(max_length=100)
    identity_proof = models.FileField(upload_to=identity_type_directory_path)
    profile_photo = models.ImageField(upload_to=profile_photo_directory_path,default="profile/avatar/blank-profile-picturepng.png") # f"{settings.MEDIA_URL}profile/avatar/blank-profile-picture.png"
    is_verified = models.IntegerField(choices=IS_VERIFIED,null=True)
    is_blocked= models.BooleanField(default=False)
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.PROTECT,null=True)
    terms = models.BooleanField(default=0)

    @property
    def full_name(self):
        if self.first_name == '':
            return None
        else:
            return f"{self.first_name} {self.last_name}"

    # account completion progress 
    REQUIRED_FIELDS_BY_GROUP = {
        "patient": [
            "username","first_name","last_name","email","nationality","gender","marital_status",
            "date_of_birth","religion","profile_photo",
            "blood_group","phone"
        ],
        "doctor": [
            "username","first_name","last_name","email","marital_status","nationality","gender",
            "date_of_birth","identity_type","identity_no","identity_proof","phone"
        ],
        "counselor": [
            "email", "phone", "profile_photo", "date_of_birth", 
            "religion", "is_verified", "terms",
        ],
    }

    
    def get_user_type(self):
        """Returns the user's group as a type identifier."""
        groups = self.groups.values_list('name', flat=True)
        for group_name in self.REQUIRED_FIELDS_BY_GROUP.keys():
            if group_name in groups:
                return group_name
        return None  # No recognized user group
    
    
    def profile_completion(self):
        calculator = UserProfileCompletion(self)
        return calculator.calculate_profile_completion()


# Address info description 
class Address(models.Model):
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,null=True,blank=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


    def __str__(self):
        return self.city
    

# Education info description
class Education(models.Model):
    institute = models.CharField(max_length=200)
    # specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,default=0)
    duration = models.CharField(max_length=20)
    passing_year = models.DateField()
    certificate = models.FileField(upload_to=education_certificate_directory_path)
    certificate_title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.institute
    

# Experience info description 
class Experience(models.Model):
    org_name  = models.CharField(max_length=200,verbose_name='Organization Name')
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,null=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    job_status = models.CharField(max_length=10,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.org_name


# Training info model description 
class Training(models.Model):
    institute = models.CharField(max_length=200)
    # specialization = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    training_title = models.CharField(max_length=200)
    training_certificate = models.FileField(upload_to=training_certificate_directory_path)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.institute

class UserProfileCompletion:
    def __init__(self, user):
        self.user = user
    def calculate_profile_completion(self):
        total_models = 0
        completed_models = 0

        # Determine user type
        user_type = self.user.get_user_type()
        if not user_type:
            return 0  # No group assigned or unrecognized group

        # Check general fields for all user types
        required_fields = self.user.REQUIRED_FIELDS_BY_GROUP.get(user_type, [])
        total_models += len(required_fields)
        completed_models += sum(1 for field in required_fields if getattr(self.user, field, None))

        

        # Role-specific checks
        if user_type == "patient":
            total_models, completed_models = self._check_address(total_models, completed_models)

        elif user_type == "doctor":
            total_models, completed_models = self._check_doctor_related_models(total_models, completed_models)

        # Avoid division by zero
        if total_models == 0:
            return 0

        # Calculate completion percentage
        return int((completed_models / total_models) * 100)

    def _check_address(self, total_models, completed_models):
        """Check address fields for patients."""
        if hasattr(self.user, 'address') and self.user.address:
            address_fields = ['address', 'zip_code', 'city', 'state', 'country']
            total_models += len(address_fields)
            completed_models += sum(1 for field in address_fields if getattr(self.user.address, field, None))
        return total_models, completed_models

    def _check_doctor_related_models(self, total_models, completed_models):
        """Check doctor-specific related models."""
        expert_fields = ['doc_title','license_no','license_attachment']
        total_models += len(expert_fields)
        if hasattr(self.user, 'expert'):
            completed_models += sum(1 for field in expert_fields if getattr(self.user.expert, field, None))


        # Education fields
        education_fields = ['institute', 'specialization', 'duration','passing_year','certificate','certificate_title']
        total_models +=len(education_fields)
        first_education = self.user.education_set.first()
        completed_models += sum(1 for field in education_fields if getattr(first_education, field, None))
        
        


        # Training fields
        training_fields = ['institute', 'specialization', 'from_date','to_date','training_title','training_certificate']
        total_models +=len(training_fields)
        first_training = self.user.training_set.first()
        completed_models += sum(1 for field in training_fields if getattr(first_training, field, None))
        

        # Experience fields
        experience_fields = ['org_name', 'department', 'designation','from_date']
        total_models +=len(experience_fields)
        first_experience = self.user.experience_set.first()
        completed_models += sum(1 for field in experience_fields if getattr(first_experience, field, None))
        
        
        return total_models, completed_models
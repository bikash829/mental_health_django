from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from pprint import pprint

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
    instance.username = instance.user.username
    return generate_upload_path(instance, filename, 'employee/education_certificates')

# training certificate 
def training_certificate_directory_path(instance, filename):
    instance.username = instance.user.username
    return generate_upload_path(instance, filename, 'employee/training_certificates')

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
        ("M", "Unmarried"),
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


    marital_status = models.CharField(max_length=2,choices=MARITAL_STATUS)
    nationality = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER)
    # phone_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    # additional_phone_code = models.CharField(max_length=10)
    additional_phone = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    religion = models.CharField(max_length=50)
    identity_type = models.IntegerField(choices=IdentityType,null=True)
    identity_no = models.CharField(max_length=100)
    identity_proof = models.FileField(upload_to=identity_type_directory_path)
    profile_photo = models.ImageField(upload_to=profile_photo_directory_path)
    is_verified = models.IntegerField(choices=IS_VERIFIED,null=True)
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.PROTECT,null=True)
    terms = models.BooleanField(default=0)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



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
    specialization = models.CharField(max_length=100)
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
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    job_status = models.CharField(max_length=10,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.org_name


# Training info model description 
class Training(models.Model):
    institute = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    training_title = models.CharField(max_length=200)
    training_certificate = models.FileField(upload_to=training_certificate_directory_path)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.institute


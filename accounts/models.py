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

# Create your models here.
class BloodGroup(models.Model):
    group = models.CharField(max_length=10)


    def __str__(self):
        return self.group


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
    phone_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    additional_phone_code = models.CharField(max_length=10)
    additional_phone = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True,blank=True)
    religion = models.CharField(max_length=50)
    identity_type = models.IntegerField(choices=IdentityType,default=0)
    identity_no = models.CharField(max_length=100)
    identity_proof = models.FileField(upload_to=identity_type_directory_path)
    profile_photo = models.ImageField(upload_to=profile_photo_directory_path)
    is_verified = models.IntegerField(choices=IS_VERIFIED,default=2)
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.PROTECT,null=True)
    terms = models.BooleanField(default=0)



from django.db import models
from django.conf import settings
from apps.accounts.models import User
from apps.accounts import models as account_models


def license_directory_path(instance, filename):
    return account_models.generate_upload_path(instance, filename, 'license_attachment')

class Expert(models.Model):
    DOC_TITLE_CHOICES = [
        (1, 'Professor Dr.'),
        (2, 'Assistant Professor Dr.'),
        (3, 'Associate Professor Dr.'),
        (4, 'Distinguished Professor Dr.'),
        (5, 'Dr.'),
    ]

    doc_title = models.IntegerField(choices=DOC_TITLE_CHOICES,null=True,blank=True,default=0 )
    license_no = models.CharField(max_length=50, )
    license_attachment = models.FileField(upload_to=license_directory_path)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


    def __str__(self):
        return self.doc_title

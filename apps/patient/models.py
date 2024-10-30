from django.db import models
from apps.accounts.models import User

# Create your models here.
class VitalSignsReport(models.Model):
    blood_pressure = models.CharField(max_length=10,blank=True)
    heart_rate = models.CharField(max_length=5,blank=True)
    sugar_level = models.FloatField(blank=True)
    checkup_date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, date: {self.checkup_date}"
    
class BiologicalInfo(models.Model):
    height = models.DecimalField(max_digits=8,decimal_places=2,blank=True)
    weight = models.DecimalField(max_digits=8,decimal_places=2,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, height: {self.height}"

from django.db import models
from apps.accounts.models import User
import datetime
# Create your models here.
class VitalSignsReport(models.Model):
    systolic  = models.PositiveIntegerField()
    diastolic   = models.PositiveIntegerField()
    heart_rate = models.CharField(max_length=5,blank=True)
    checkup_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, date: {self.checkup_date}"

class BloodSugar(models.Model):
    sugar_level = models.FloatField(blank=True)
    checkup_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Sugar Level: {self.sugar_level}"

class BiologicalInfo(models.Model):
    height = models.DecimalField(max_digits=8,decimal_places=2,blank=True,help_text="Height in cm")
    weight = models.DecimalField(max_digits=8,decimal_places=2,blank=True,help_text="Weight in kg")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, height: {self.height}"

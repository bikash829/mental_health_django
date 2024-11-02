from django.contrib import admin
from .models import VitalSignsReport,BloodSugar,BiologicalInfo
# Register your models here.


admin.site.register(VitalSignsReport)


admin.site.register(BloodSugar)

admin.site.register(BiologicalInfo)
from django.urls import path
from apps.doctor_dashboard import views

app_name = 'doctor'

urlpatterns = [
    path('',views.index,name='index'),
]

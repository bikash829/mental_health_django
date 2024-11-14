from django.urls import path
from apps.doctor_dashboard import views

urlpatterns = [
    path('',views.index,name='index'),
]

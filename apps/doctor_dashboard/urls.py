from django.urls import path
from apps.doctor_dashboard import views

app_name = 'doctor'

urlpatterns = [
    path('',views.index,name='dashboard'),
    path('profile_update/',views.profile_update,name="profile_update"),
]

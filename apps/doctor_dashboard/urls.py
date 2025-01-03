from django.urls import path
from apps.doctor_dashboard import views

app_name = 'doctor'

urlpatterns = [
    path('',views.index,name='dashboard'),
    path('profile_update/',views.profile_update,name="profile_update"),
    path('initial_data/', views.update_initial_info, name='update_initial_info'),
    path('education_info/', views.update_education_info, name='update_education_info'),
    path('delete_education/', views.delete_education, name='delete_education'),
    # training 
    path('update_training/', views.update_training, name='update_training'),
    path('delete_training/', views.delete_training, name='delete_training'),
    # experience 
    path('update_experience/',views.update_experience,name='update_experience'),
    path('delete_experience/',views.delete_experience,name='delete_experience'),
    # profile
    path('profile/',views.profile,name='profile'),

]

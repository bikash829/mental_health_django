from django.urls import path
from . import views 
app_name='patient'

urlpatterns = [
    path('edit_basic_info/',views.edit_basic_info,name="edit_basic_info"),
    path('edit_address/',views.edit_address,name="edit_address"),
    path('edit_contact/',views.edit_contact,name="edit_contact"),
    path('update_vital_sign_info/',views.update_vital_sign_info,name="update_vital_sign_info"),
    path('update_blood_sugar_info/',views.update_blood_sugar_info,name="update_blood_sugar_info"),
    path('update_biological_info/<int:id>/',views.update_biological_info,name="update_biological_info"),
]
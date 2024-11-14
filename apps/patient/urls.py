from django.urls import path
from . import views 
app_name='patient'

urlpatterns = [
    path('edit_basic_info/',views.edit_basic_info,name="edit_basic_info"),
    path('edit_address/',views.edit_address,name="edit_address"),
    path('edit_contact/',views.edit_contact,name="edit_contact"),
    path('add_vital_sign_info/',views.add_vital_sign_info,name="add_vital_sign_info"),
    path('delete_vital_sign_report/<int:id>/',views.delete_vital_sign_report,name="delete_vital_sign_report"),
    path('add_blood_sugar_info/',views.add_blood_sugar_info,name="add_blood_sugar_info"),
    path('delete_blood_sugar_report/<int:id>/',views.delete_blood_sugar_report,name="delete_blood_sugar_report"),
    path('add_biological_info/',views.add_biological_info,name="add_biological_info"),
    path('update_biological_info/<int:id>/',views.update_biological_info,name="update_biological_info"),
]
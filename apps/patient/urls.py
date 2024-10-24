from django.urls import path
from . import views 
app_name='patient'

urlpatterns = [
    path('edit_basic_info/',views.edit_basic_info,name="edit_basic_info"),
    path('edit_address/',views.edit_address,name="edit_address"),
]
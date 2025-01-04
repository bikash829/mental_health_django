from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('welcome/',views.index,name='welcome'),
]
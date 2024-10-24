
from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('noboard/',views.noboard,name="noboard"),
    path('level1/',views.level1,name="level1"),
    path('change_mail/',views.change_mail,name="change_mail"),

]

from django.urls import path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('profile/',views.profile,name="profile"),
    path('change_profile_photo/',views.change_profile_photo,name='change_profile_photo')

    # path('sign_up/', views.sign_up,name="sign_up"),
    # path('profile/',views.profile,name="profile"),
]
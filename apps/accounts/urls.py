from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'
urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'), # must maintain order
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path("", include("django.contrib.auth.urls")),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
        
    path('profile/',views.profile,name="profile"),
    path('change_profile_photo/',views.change_profile_photo,name='change_profile_photo'),
    
]
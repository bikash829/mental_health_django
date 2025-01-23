from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('',views.index,name='dashboard'),
    # Manage users 
    path('pending-users/',views.PendingUserListView.as_view(),name='pending_users'),
    path('user-details/<int:pk>/', views.ShowUserProfileDetails.as_view(), name='show_profile_details'),

]
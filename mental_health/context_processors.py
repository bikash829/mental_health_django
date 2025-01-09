from apps.dashboard.aside_items import get_sidebar_items
from django.urls import reverse
from apps.doctor_dashboard import nav_assets
from apps.admin_dashboard import nav_assets as admin_nav

def sidebar_items(request):
    # if request.user.is_authenticated:
    #     role = request.user.role  # Assuming you have a way to get the user's role
    #     sidebar_items = get_sidebar_items(request, role)
    # else:
    #     sidebar_items = []
    if request.user.groups.filter(name='doctor').exists():
        nav_assets_data = nav_assets.nav_assets(request)
    elif request.user.groups.filter(name='counselor').exists():
        nav_assets_data = {}
    elif request.user.is_superuser:
        nav_assets_data = admin_nav.nav_assets(request)
    else:
        nav_assets_data = {}



    sidebar_items = get_sidebar_items(request)
    
    return {'sidebar_items': sidebar_items,'top_nav': nav_assets_data}
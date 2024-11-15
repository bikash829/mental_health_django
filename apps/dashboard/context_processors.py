from .aside_items import get_sidebar_items
from django.urls import reverse


def sidebar_items(request):
    # if request.user.is_authenticated:
    #     role = request.user.role  # Assuming you have a way to get the user's role
    #     sidebar_items = get_sidebar_items(request, role)
    # else:
    #     sidebar_items = []
    sidebar_items = get_sidebar_items(request)
    
    return {'sidebar_items': sidebar_items,'dashboard_url':''}
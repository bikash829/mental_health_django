from .utils import get_sidebar_items

def sidebar_items(request):
    # if request.user.is_authenticated:
    #     role = request.user.role  # Assuming you have a way to get the user's role
    #     sidebar_items = get_sidebar_items(request, role)
    # else:
    #     sidebar_items = []
    sidebar_items = get_sidebar_items(request)
    
    return {'sidebar_items': sidebar_items}
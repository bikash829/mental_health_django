from django.shortcuts import render
from django.urls import reverse
import pprint

def mark_active_sidebar_items(items, current_path):
    # Flag to indicate if any item in the current list is active
    any_active = False

    for item in items:
        # Mark the item active if its URL matches the current request path
        item['is_active'] = current_path == item['url']
        
        # Recursively check for active children if the item has children
        if 'children' in item and item['children']:
            item['children'], child_active = mark_active_sidebar_items(item['children'], current_path)
            item['is_active'] = item['is_active'] or child_active  # Mark parent active if any child is active

        # If this item or any of its children are active, flag it
        any_active = any_active or item['is_active']

    return items, any_active


# Create your views here.
def dashboard(request):
    sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('dashboard:dashboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Widgets',
            'url': '/blash/#',
            'icon': 'nav-icon bi bi-box-seam-fill',
            'children': [
                {
                    'name': 'Small Box',
                    'url': reverse('dashboard:level1'),
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)

    
    
    
    template_name = "dashboard/pages/index.html"
    context = {
        'sidebar_items' : sidebar_items,
    }
    pprint.pprint(context)


    return render(request,template_name,context)


def noboard(request):
    sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('dashboard:dashboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Widgets',
            'url': '#',
            'icon': 'nav-icon bi bi-box-seam-fill',
            'children': [
                {
                    'name': 'Small Box',
                    'url': reverse('dashboard:level1'),
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)

    template_name = "dashboard/pages/noboard.html"
    context = {
        'sidebar_items' : sidebar_items,
    }

    pprint.pprint(context)
    
    return render(request,template_name,context)

def level1(request):
    
    sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('dashboard:dashboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Widgets',
            'url': '#',
            'icon': 'nav-icon bi bi-box-seam-fill',
            'children': [
                {
                    'name': 'Small Box',
                    'url': reverse('dashboard:level1'),
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)

    template_name = "dashboard/pages/level1.html"
    context = {
        'sidebar_items': sidebar_items,
    }
    pprint.pprint(context)
    return render(request,template_name,context)

def change_mail(request):
    
    sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('dashboard:dashboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
            # 'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Widgets',
            'url': '#',
            'icon': 'nav-icon bi bi-box-seam-fill',
            'children': [
                {
                    'name': 'Small Box',
                    'url': reverse('dashboard:level1'),
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)

    template_name = "dashboard/pages/change_mail.html"
    context = {
        'sidebar_items': sidebar_items,
    }
    pprint.pprint(context)
    return render(request,template_name,context)
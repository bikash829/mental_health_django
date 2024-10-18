from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def dashboard(request):
    template_name = "dashboard/pages/index.html"
    context = {
        'sidebar_items' : [
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
                    'url': '#',
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': '#', 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    }
    return render(request,template_name,context)


def noboard(request):
    template_name = "dashboard/pages/noboard.html"
    context = {
        'sidebar_items' : [
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
                    'url': '#',
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': '#', 'icon': 'bi bi-record-circle-fill',},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill',}
                    ]
                }
            ]
        }
    ]
    }
    return render(request,template_name,context)
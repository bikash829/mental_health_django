# utils.py
from django.urls import reverse

def mark_active_sidebar_items(items, current_path):
    any_active = False

    for item in items:
        item['is_active'] = current_path == item['url']
        
        if 'children' in item and item['children']:
            item['children'], child_active = mark_active_sidebar_items(item['children'], current_path)
            item['is_active'] = item['is_active'] or child_active

        any_active = any_active or item['is_active']

    return items, any_active

def get_admin_sidebar_items(request):
    sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('dashboard:dashboard'),
            'icon': 'bi bi-speedometer',
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
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
                    'name': 'Info Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    'children': [
                        {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill'},
                        {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill'},
                    ]
                }
            ]
        }
    ]
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)
    return sidebar_items
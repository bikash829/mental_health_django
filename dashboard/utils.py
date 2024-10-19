# utils.py
from django.urls import reverse

# Create sidebar items
def mark_active_sidebar_items(items, current_path):
    any_active = False

    for item in items:
        item['is_active'] = current_path == item['url']
        
        if 'children' in item and item['children']:
            item['children'], child_active = mark_active_sidebar_items(item['children'], current_path)
            item['is_active'] = item['is_active'] or child_active

        any_active = any_active or item['is_active']

    return items, any_active

def get_sidebar_items(request):
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
            'divider_header': 'EXAMPLES',
            'url': None,
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

    # counselor_sidebar_items = [
    #     {
    #         'name': 'Sessions',
    #         'url': reverse('counselor:sessions'),
    #         'icon': 'bi bi-chat-dots',
    #     },
    #     {
    #         'name': 'Reports',
    #         'url': reverse('counselor:reports'),
    #         'icon': 'bi bi-file-earmark-text',
    #     }
    # ]

    # if role == 'admin':
    #     sidebar_items = admin_sidebar_items
    # elif role == 'doctor':
    #     sidebar_items = doctor_sidebar_items
    # elif role == 'counselor':
    #     sidebar_items = counselor_sidebar_items
    # else:
    #     sidebar_items = []
    sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)
    return sidebar_items
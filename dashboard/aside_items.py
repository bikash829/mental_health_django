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
        },{
            'divider_header': 'Appointments',
            'url': None,
        },
        {
            'name': 'Active Patient Appointments',
            'url': None,
            'icon': 'fa-solid fa-calendar-check',
        },
        {
            'name': 'Past Appointments',
            'url': None,
            'icon': 'fa-solid fa-hourglass-end',
        },
        {
            'name': 'Noboard',
            'url': reverse('dashboard:noboard'),
            'icon': 'bi bi-speedometer',
        },
        {
            'divider_header': 'Doctor Schedules',
            'url': None,
        },
        {
            'name': 'Doctor Appointment Schedules',
            'url': None,
            'icon': 'fa-solid fa-calendar-check',
        },
        {
            'divider_header': 'Users',
            'url': None,
        },
        {
            'name': 'Manage User',
            'url': None,
            'icon': 'fa-solid fa-screwdriver-wrench',
            'children':[
                {
                    'name': 'Pending Experts',
                    'url': None,
                    'icon': 'fa-solid fa-hourglass-end',
                },
                {
                    'name': 'Blocked User',
                    'url': None,
                    'icon': 'fa-solid fa-ban',
                },
                {
                    'name': 'Doctors',
                    'url': None,
                    'icon': 'fa-solid fa-user-doctor',
                },
                {
                    'name': 'Counselors',
                    'url': None,
                    'icon': 'fa-solid fa-headset',
                },
                {
                    'name': 'Patients',
                    'url': None,
                    'icon': 'fa-solid fa-bed-pulse',
                },
                {
                    'name': 'All User',
                    'url': None,
                    'icon': 'fa-solid fa-user-group',
                },
            ]
        },
        {
            'divider_header': 'Community',
            'url': None,
        },
        {
            'name': 'Community Forum',
            'url': None,
            'icon': 'fa-solid fa-users'
        },
        {
            'divider_header': 'Notifications and Messages',
            'url': None,
        },
        {
            'name': 'Contact Us Query',
            'url' : None,
            'icon': 'fa-solid fa-envelope',
        },
        # {
        #     'name': 'Widgets',
        #     'url': '#',
        #     'icon': 'nav-icon bi bi-box-seam-fill',
        #     'children': [
        #         {
        #             'name': 'Small Box',
        #             'url': reverse('dashboard:level1'),
        #             'icon': 'bi bi-circle',
        #         },
        #         {
        #             'name': 'Info Box',
        #             'url': '#',
        #             'icon': 'bi bi-circle',
        #             'children': [
        #                 {'name': 'Change Email', 'url': reverse('dashboard:change_mail'), 'icon': 'bi bi-record-circle-fill'},
        #                 {'name': 'Two Factor Auth', 'url': '#', 'icon': 'bi bi-record-circle-fill'},
        #             ]
        #         }
        #     ]
        # }
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
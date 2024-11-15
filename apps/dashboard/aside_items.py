# utils.py
from django.urls import reverse
from django.contrib.auth.models import Group

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
    ]


    # Doctor sidebar
    doctor_sidebar_items = [
        {
            'name': 'Dashboard',
            'url': reverse('doctor:dashboard'),
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
            'divider_header': 'Community',
            'url': None,
        },
        {
            'name': 'Community Forum',
            'url': None,
            'icon': 'fa-solid fa-users'
        },
    ]
    # counselor sidebar
    counselor_sidebar_items = [
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
            'divider_header': 'Community',
            'url': None,
        },
        {
            'name': 'Community Forum',
            'url': None,
            'icon': 'fa-solid fa-users'
        },
       

    ]

    if request.user.groups.filter(name='doctor').exists():
        sidebar_items, _ = mark_active_sidebar_items(doctor_sidebar_items, request.path)
    elif request.user.groups.filter(name='counselor').exists():
        sidebar_items, _ = mark_active_sidebar_items(counselor_sidebar_items, request.path)
    elif request.user.groups.filter(name='admin').exists():
        sidebar_items, _ = mark_active_sidebar_items(sidebar_items, request.path)
    # else:
    #     sidebar_items, _ = []

    
    return sidebar_items
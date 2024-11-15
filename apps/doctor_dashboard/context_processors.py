from django.urls import reverse

def nav_assets_processor(request):
    nav_assets={
        'start_menu_items':[
            {
                'name': 'Home',
                'url': reverse('doctor:dashboard')
            },
            {
                'name': 'Contact',
                'url': None
            }
        ],
        'end_menu_items':{
            'messages':[
                {
                    'divider': False,
                    'url': None,
                    'user_avatar': 'dashboard/assets/img/user8-128x128.jpg',
                    'avatar_alt': 'something alternet',
                    'user_name': 'John Pierce',
                    'message': 'I got your message bro',
                    'time' : '4 Hours Ago',
                },
                {
                    'divider': True,
                    'user_avatar': 'dashboard/assets/img/user8-128x128.jpg',
                    'avatar_alt': 'something alternet',
                    'user_name': 'Rango',
                    'message': 'Yoo! what\'s up?',
                    'time' : '10 Hours Ago',
                },
            ],
            'notifications':{
                'total_notifications': 15,
                'notification_list':[
                    {
                        'url': None,
                        'icon': 'bi bi-envelope',
                        'notification_count': 5,
                        'notification_from': 'new messages',
                        'time': '3 mins'

                    },
                    {
                        'url': None,
                        'icon': 'bi bi-people-fill',
                        'notification_count': 8,
                        'notification_from': 'friend requests',
                        'time': '12 hour'

                    },
                    {
                        'url': None,
                        'icon': 'bi bi-people-fill',
                        'notification_count': 3,
                        'notification_from': 'new reports',
                        'time': '2 days'
                    }
                ]
            }
        },
        'self_info':{
            'name': 'Alexander Pierce',
            'photo': 'dashboard/assets/img/user2-160x160.jpg',
            'photo_alt': 'something user',
            'designation': 'Web Developer',
            'member_from': 'Nov. 2023',
            'profile_link': None,
        }
     
    }

    return {'top_nav': nav_assets}
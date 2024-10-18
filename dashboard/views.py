from django.shortcuts import render

# Create your views here.
def dashboard(request):
    template_name = "dashboard/pages/index.html"
    context = {
        'sidebar_items' : [
        {
            'name': 'Dashboard',
            'url': '/dashboard/',
            'icon': 'bi bi-speedometer',
            
        },
        {
            'name': 'Widgets',
            'url': '/dashboard/#',
            'icon': 'nav-icon bi bi-box-seam-fill',
            'children': [
                {
                    'name': 'Small Box',
                    'url': '#',
                    'icon': 'bi bi-circle',
                    
                },
                {
                    'name': 'info Box',
                    'url': '/dashboard/#',
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

from django.shortcuts import render
from .aside_items import get_sidebar_items


# Create your views here.
def dashboard(request):
    # sidebar_items = get_sidebar_items(request)
    
    template_name = "dashboard/pages/index.html"
    context = {
        # 'sidebar_items' : sidebar_items,
    }

    return render(request,template_name,context)


def noboard(request):
    # sidebar_items = get_sidebar_items(request)
    template_name = "dashboard/pages/noboard.html"
    context = {
        # 'sidebar_items' : sidebar_items,
    }
    
    return render(request,template_name,context)


def level1(request):
    
    # sidebar_items = get_sidebar_items(request)

    template_name = "dashboard/pages/level1.html"
    context = {
        # 'sidebar_items': sidebar_items,
    }
    
    return render(request,template_name,context)


def change_mail(request):
    
    # sidebar_items = get_sidebar_items(request)

    template_name = "dashboard/pages/change_mail.html"
    context = {
        # 'sidebar_items': sidebar_items,
    }

    return render(request,template_name,context)
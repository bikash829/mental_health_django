from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    
    template_name = "admin_dashboard/dashboard.html"
    context={

    }
    return render(request,template_name,context)


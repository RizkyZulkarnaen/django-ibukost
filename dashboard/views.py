from django.shortcuts import render
from .models import data_kost, user_kost

# Create your views here.
def log(request):
    return render(request, 'dashboard/logging.html',{
        'title': 'Logging'
    })

def dashboard(request):
    return render(request, 'dashboard/dashboard.html',{
        'title': 'Dashboard'
    })
    
def add_kost(request):
    return render(request, 'dashboard/kost/add_kost.html',{
        'title': 'Add Kost'
    })
    
def list_kost(request):
    kost = data_kost.objects.all()
    return render(request, 'dashboard/kost/list_kost.html',{
        'title': 'list Kost',
        'Kost': kost,
    })

def add_user(request):
    return render(request, 'dashboard/users/add_user.html',{
        'title': 'Add user'
    })
    
def list_user(request):
    return render(request, 'dashboard/users/list_user.html',{
        'title': 'list user'
    })
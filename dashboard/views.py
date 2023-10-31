from django.shortcuts import render
from .models import kost_member, user_member

# Create your views here.
def log(request):
    return render(request, 'dashboard/logging.html',{
        'title': 'Logging'
    })

def dashboard(request):
    total_kost = kost_member.objects.count()
    total_user = user_member.objects.count()
    return render(request, 'dashboard/dashboard.html',{
        'title': 'Dashboard',
        'total_kost': total_kost,
        'total_user': total_user,
    })
    
def add_kost(request):
    return render(request, 'dashboard/kost/add_kost.html',{
        'title': 'Add Kost'
    })
    
def list_kost(request):
    kost = kost_member.objects.all()
    return render(request, 'dashboard/kost/list_kost.html',{
        'title': 'list Kost',
        'Kost': kost,
    })

def add_user(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('code_user') and request.POST.get('tag_id') and request.POST.get('telepon') and request.POST.get('alamat'):
            post = user_member()
            post.username = request.POST.get('username')
            post.unique_id = request.POST.get('code_user')
            post.telepon = request.POST.get('telepon')
            post.alamat = request.POST.get('alamat')
            post.save()
            
            return render(request, 'dashboard/users/add_user.html',{
                'title': 'Add user'
            })
    else:
        return render(request, 'dashboard/users/add_user.html',{
                'title': 'Add user'
            })
def list_user(request):
    user = user_member.objects.all()
    return render(request, 'dashboard/users/list_user.html',{
        'title': 'list user',
        'User': user,
    })
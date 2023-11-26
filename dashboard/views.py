from typing import Any
from django.shortcuts import render, redirect
from .models import kost_member, user_member
from .forms import user_form, kost_form
from django.views.generic.base import TemplateView

# Create your views here.

class index_views(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title_list_kost': 'List Kost',
            'title_list_user': 'List User',
            'title_log': 'Logging',
            'model_user': user_member.objects.all(),
            'model_kost': kost_member.objects.all(),
        })
        return context

def dashboard_views(request):
    joined = {}
    total_kost = kost_member.objects.count()
    total_user = user_member.objects.count()
    data_kost_member = kost_member.objects.all()
    data_user_member = user_member.objects.all()

    # Gabungkan data berdasarkan field unique_id
    for item_kost_member in data_kost_member:
        items_user_member = data_user_member.filter(unique_id=item_kost_member.unique_id)
        for item_user_member in items_user_member:
            # Kunci unik berdasarkan kombinasi nama_kost dan username
            key = f'{item_kost_member.nama_kost}_{item_user_member.username}'

            # Jika data ditemukan, gabungkan dan tambahkan ke joined
            if key not in joined:
                joined[key] = {
                    'nama_kost': item_kost_member.nama_kost,
                    'unique_id': item_kost_member.unique_id,
                    'nomor_kost': item_kost_member.nomor_kost,
                    'status': item_kost_member.status,
                    'username': item_user_member.username,
                    'tag_id': item_user_member.tag_id,
                    'telepon': item_user_member.telepon,
                    'alamat': item_user_member.alamat,
                }
                
    context = {
        'title_dasboard': 'Dashboard',
        'total_kost': total_kost,
        'total_user': total_user,
        'joined': joined.items(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def add_kost(request):
    form = kost_form()
    if request.method == 'POST':
        kost_member.objects.create(
            nama_kost = request.POST.get('nama_kost'),
            nomor_kost = request.POST.get('nomor_kost'),
            unique_id = request.POST.get('unique_id'),
            status = request.POST.get('status'),
        )
    context = {
        'title': 'Add Kost',
        'form': form,
    }
    return render(request, 'dashboard/kost/add_kost.html',context)

def delete_kost(request, id):
    kost = kost_member.objects.get(id=id)
    kost.delete()
    return redirect('list_kost')

def update_kost(request, id):
    kost = kost_member.objects.get(id=id)
    form = kost_form(instance=kost)
    if request.method == 'POST':
        form = kost_form(request.POST, instance=kost)
        if form.is_valid():
            form.save()
            return redirect('list_kost')
    context = {
        'title': 'Update Kost',
        'form': form,
    }
    return render(request, 'dashboard/kost/update_kost.html', context)

def add_user(request):
    form = user_form()
    if request.method == 'POST':
        user_member.objects.create(
            username = request.POST.get('username'),
            tag_id = request.POST.get('tag_id'),
            unique_id = request.POST.get('unique_id'),
            telepon = request.POST.get('telepon'),
            alamat = request.POST.get('alamat'),
        )
    context = {    
    'title': 'Add user',
    'form':form,
    }
    
    return render(request, 'dashboard/users/add_user.html',context)

def delete_user(request, id):
    user = user_member.objects.get(id=id)
    user.delete()
    return redirect('list_user')

def update_user(request, id):
    user = user_member.objects.get(id=id)
    form = user_form(instance=user)
    if request.method == 'POST':
        form = user_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    context = {
        'title': 'Update User',
        'form': form,
    }
    return render(request, 'dashboard/users/update_user.html', context)
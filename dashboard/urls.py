from django.urls import path
from .views import log, dashboard, add_kost, list_kost, add_user, list_user

urlpatterns = [
    path('log/', log, name='log'),
    path('', dashboard, name='dashboard'),
    path('addkost/', add_kost, name='add_kost'),
    path('listkost/', list_kost, name='list_kost'),
    path('adduser/', add_user, name='add_user'),
    path('listuser/', list_user, name='list_user'),
]

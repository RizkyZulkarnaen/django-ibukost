from django.urls import path
from . import views
from .views import index_views

urlpatterns = [
    path('', views.dashboard_views, name='dashboard'),
    path('log/', index_views.as_view(template_name='dashboard/logging.html'), name='log'),
    path('addkost/', views.add_kost, name='add_kost'),
    path('listkost/', index_views.as_view(template_name='dashboard/kost/list_kost.html'), name='list_kost'),
    path('updatekost/<str:id>/', views.update_kost, name='update_kost'),
    path('deletekost/<str:id>/', views.delete_kost, name='delete_kost'),
    path('adduser/', views.add_user, name='add_user'),
    path('listuser/', index_views.as_view(template_name='dashboard/users/list_user.html'), name='list_user'),
    path('updateuser/<str:id>/', views.update_user, name='update_user'),
    path('deleteuser/<str:id>/', views.delete_user, name='delete_user'),
]

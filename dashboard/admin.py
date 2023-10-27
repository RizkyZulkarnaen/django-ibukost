from django.contrib import admin

# Register your models here.
from .models import data_kost, user_kost

admin.site.register(data_kost)
admin.site.register(user_kost)
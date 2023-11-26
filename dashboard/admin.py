from django.contrib import admin

# Register your models here.
from .models import kost_member, user_member

admin.site.register(kost_member)
admin.site.register(user_member)
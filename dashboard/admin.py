from django.contrib import admin

# Register your models here.
from .models import kost_member, user_member, tag_rfid

admin.site.register(kost_member)
admin.site.register(user_member)
admin.site.register(tag_rfid)
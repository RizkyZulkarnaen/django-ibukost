from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import kost_member, user_member

@receiver(post_save, sender=kost_member)
@receiver(post_save, sender=user_member)
def reload_data(sender, instance, **kwargs):
    # Ambil dan muat ulang data sesuai kebutuhan
    if sender == kost_member:
        kost_data = kost_member.objects.all()
        # Lakukan sesuatu dengan data kost jika diperlukan

    elif sender == user_member:
        user_data = user_member.objects.all()
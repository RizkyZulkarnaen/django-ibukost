from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class kost_member(models.Model):
    nama_kost = models.CharField(max_length=255)
    nomor_kost = models.CharField(max_length=50)
    unique_id = models.IntegerField()
    STATUS_CHOICES = (
            ('open','Open'),
            ('close','Close'),
        )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='close')
    
    def __str__(self):
        return "{}".format(self.nama_kost)
    
class user_member(models.Model):
    username = models.CharField(max_length=255)
    tag_id = models.BigIntegerField()
    unique_id = models.IntegerField()
    telepon = models.BigIntegerField(validators=[MaxValueValidator(999999999999), MinValueValidator(9999999999)])
    alamat = models.CharField(max_length=255,blank=True)
        
    def __str__(self):
        return "{}".format(self.username)
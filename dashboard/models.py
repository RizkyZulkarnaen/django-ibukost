from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class kost_member(models.Model):
    nama_kost = models.CharField(max_length=255)
    nomor_kost = models.CharField(max_length=50,default=0)
    unique_id = models.IntegerField()
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}".format(self.nama_kost)
    
class user_member(models.Model):
    username = models.CharField(max_length=255)
    unique_id = models.IntegerField()
    telepon = models.BigIntegerField(validators=[MaxValueValidator(999999999999), MinValueValidator(9999999999)])
    alamat = models.CharField(max_length=255)
        
    def __str__(self):
        return "{}".format(self.username)

class tag_rfid(models.Model):
    tag_id = models.IntegerField()
    unique_id = models.IntegerField(default=0)
    
    def __str__(self):
        return "{}".format(self.tag_id)
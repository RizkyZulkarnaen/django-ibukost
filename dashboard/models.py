from django.db import models

# Create your models here.
class data_kost(models.Model):
    nama_kost = models.CharField(max_length=255)
    nomor_kost = models.CharField(max_length=50,default=0)
    code_kost = models.IntegerField()
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}".format(self.nama_kost)
    
class user_kost(models.Model):
    username = models.CharField(max_length=255)
    code_user = models.IntegerField()
    tag_id = models.IntegerField()
    telepon = models.IntegerField()
    alamat = models.CharField(max_length=255)
    
    def __str__(self):
        return "{}".format(self.username)
from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Etkinlik(models.Model):
    name=models.CharField(max_length=100,)
    koordinator=models.CharField(max_length=100,blank=True,null=True)
    etkinlik_tarihi=models.DateTimeField()
    duyuru_tarihi=models.DateTimeField(auto_now_add=True)
    konum=models.CharField(max_length=100,blank=True)
    aciklama=models.TextField()
    icerik=models.CharField(max_length=90,blank=True) 

    def __str__(self) -> str:
        return self.name

class Profil(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profiller')
    okul_numara=models.CharField(max_length=10,unique=True,null=True)
    telefon_numarasi=models.CharField(max_length=11,unique=True,null=True)
    bolum=models.CharField(max_length=50,null=True)
    siniflar=[('0','Hazırlık Sınıfı'),('1','Birinci Sınıf'),('2','İkinci Sınıf'),('3','Üçüncü Sınıf'),('4','Dördüncü Sınıf'),('4+','4+')]
    sinif=models.CharField(max_length=20,choices=siniflar,default=0)

from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EtkinlikModel(models.Model):
    name=models.CharField(max_length=100,)
    koordinator=models.CharField(max_length=100,blank=True,null=True)
    etkinlik_tarihi=models.DateTimeField()
    duyuru_tarihi=models.DateTimeField(auto_now_add=True)
    konum=models.CharField(max_length=100,blank=True)
    aciklama=models.TextField()
    icerik=models.CharField(max_length=90,blank=True) 


    def __str__(self) -> str:
        return self.name

class ProfilModel(models.Model):
    isim=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profiller')
    hakkinda=models.CharField(max_length=290,null=True,blank=True)
    okul_numara=models.CharField(max_length=10,unique=True,null=True)
    telefon_numarasi=models.CharField(max_length=11,unique=True,null=True)
    bolum=models.CharField(max_length=50,null=True)
    siniflar=[('0','Hazırlık Sınıfı'),('1','Birinci Sınıf'),('2','İkinci Sınıf'),('3','Üçüncü Sınıf'),('4','Dördüncü Sınıf'),('4+','4+')]
    sinif=models.CharField(max_length=20,choices=siniflar,default=0)
    hes_kod=models.CharField(max_length=15,unique=True,null=True)
    katki=models.BooleanField(default=False,)
    kayit_tarihi=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self) -> str:
        return self.user.username


class MalzemeModel(models.Model):
    isim=models.CharField(max_length=100,)
    adet=models.PositiveIntegerField(default=1,)
    durum=models.BooleanField(default=True,)
    fiyat=models.PositiveIntegerField(null=True,blank=True)
    alindigi_tarih=models.DateField(null=True,blank=True)

    def __str__(self) -> str:
        return self.isim


class KitapModel(models.Model):
    isim=models.CharField(max_length=50,)
    sahip=models.ForeignKey(ProfilModel,on_delete=models.PROTECT,related_name='kitaplar',default=None)
    sayfa_sayisi=models.IntegerField(null=True)
    icerik=models.TextField(null=True,blank=True)
    yazarin_adi=models.CharField(max_length=50,null=True,blank=True)
    verildigi_tarih=models.DateField(null=True)
    alinacagi_tarih=models.DateField(null=True)
    durum=models.BooleanField(default=True,null=True)


    def __str__(self) -> str:
        return self.isim
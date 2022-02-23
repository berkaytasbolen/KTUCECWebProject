from django.contrib import admin
from .models import EtkinlikModel, KitapModel, ProfilModel
# Register your models here.

admin.site.register(EtkinlikModel)
admin.site.register(ProfilModel)
admin.site.register(KitapModel)

from django.contrib import admin
from .models import Topico, Webpage, RegistroAcesso, Pessoa

# Register your models here.

admin.site.register(Topico)
admin.site.register(Webpage)
admin.site.register(RegistroAcesso)
admin.site.register(Pessoa)

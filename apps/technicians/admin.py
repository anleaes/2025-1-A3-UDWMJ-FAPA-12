from django.contrib import admin
from .models import Tecnico


# Register your models here.

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especializacao')



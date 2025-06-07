from django.contrib import admin
from .models import Peca


# Register your models here.

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'custo_unitario')

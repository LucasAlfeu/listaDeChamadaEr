from django.contrib import admin
from chamada.models import Chamada

class ListandoEmbaixadores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'presenca')
    list_display_links = ('nome', 'presenca')
    

admin.site.register(Chamada, ListandoEmbaixadores)

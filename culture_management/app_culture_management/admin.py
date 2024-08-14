from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data_inicio', 'data_fim', 'horario', 'local', 'cidade', 'valor', 'entrada_gratuita', 'vagas')
    list_filter = ('tipo', 'data_inicio', 'data_fim', 'cidade')
    search_fields = ('titulo', 'local', 'cidade')

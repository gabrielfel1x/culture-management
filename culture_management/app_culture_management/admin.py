from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data', 'horario', 'local', 'cidade', 'valor', 'entrada_gratuita', 'vagas')
    list_filter = ('tipo', 'data', 'cidade')
    search_fields = ('titulo', 'local', 'cidade')

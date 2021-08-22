from django.contrib import admin
from .models import Pregunta, Respuesta


class RespuestaInLine(admin.TabularInline):
    model = Respuesta


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInLine]
    list_display = ["texto", "categoria"] # columnas que muestra la grilla
    search_fields = ["texto"]  # Buscado encima
    list_filter = ["categoria"]  # Filtro a la derecha
    ordering = ["id"]
    list_per_page = 8


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ["texto", "pregunta", "correcta"]
    ordering = ["pregunta", "-correcta"]
    list_filter = ["correcta"]  # Filtro a la derecha

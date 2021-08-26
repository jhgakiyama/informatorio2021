from django.contrib import admin
from .models import Pregunta, Respuesta


class RespuestaInLine(admin.TabularInline):
    model = Respuesta


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInLine]
    list_display = ["texto", "categoria", "cant_rtas", "cant_rtas_ok"]  # columnas que muestra la grilla
    search_fields = ["texto"]  # Buscado encima
    list_filter = ["categoria"]  # Filtro a la derecha
    ordering = ["id"]
    list_per_page = 8


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ["texto", "short", "correcta"]
    ordering = ["pregunta", "-correcta"]
    list_filter = ["correcta"]  # Filtro a la derecha
    list_per_page = 9


admin.site.site_header = "Trivia Chaco 2021 | Admin Ver 1.0.0"
admin.site.index_title = "Trivia Chaco 2021 | Admin Dashboard"

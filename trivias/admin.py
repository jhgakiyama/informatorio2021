from django.contrib import admin
from .models import Juego


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nivel", "fecha", "puntaje"]  # columnas de la grilla
    list_filter = ["user", "nivel"]
    list_editable = ["nivel", "puntaje"]
    list_per_page = 10

# @admin.register(Trivia)
# class TriviaAdmin(admin.ModelAdmin):
#     filter_horizontal = ["pregunta"]  # muestro 2 columnas para seleccionar las preguntas
#     list_display = ["id", "nivel", "fecha"]  # columnas de la grilla
#     list_filter = ["nivel"]  # filtro a la derecha
#
#
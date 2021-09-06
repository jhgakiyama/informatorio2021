from django.contrib import admin
from .models import Pregunta, Respuesta


# class CantRtasFilter(admin.SimpleListFilter):
#     """
#         No me sirve porque los query los tengo que
#         hacer sobre atributos fisico.
#     """
#     title = "# Rtas Verdadera"
#     parameter_name = "cant_rtas"
#
#     def lookups(self, request, model_admin):
#         return (
#             # (el valor que devuelve la queryset, lo que va a decir la dcha),
#             ('1', '1'),
#             ('2', '2 o mas'),
#         )
#
#     def queryset(self, request, queryset):
#         if not self.value():
#             return queryset
#         if self.value() == '1':
#             return queryset.filter(cant_rtas=1)
#         else:
#             return queryset.exclude(cant_rtas=1)
#

class RespuestaInLine(admin.TabularInline):
    model = Respuesta


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInLine]
    list_display = ["id", "texto", "nivel", "categoria", "cant_rtas", "get_respuestas_ok"]  #  muestra la grilla
    list_editable = ["nivel", "categoria"]  # editor en grilla
    search_fields = ["texto"]  # Buscado encima
    list_filter = ["nivel", "categoria"]  # Filtro a la derecha
    ordering = ["id"]
    list_per_page = 8


# @admin.register(Respuesta)
# class RespuestaAdmin(admin.ModelAdmin):
#     list_display = ["texto", "short", "correcta"]
#     ordering = ["pregunta", "-correcta"]
#     list_filter = ["correcta"]  # Filtro a la derecha
#     list_per_page = 9


admin.site.site_header = "Trivia Chaco 2021 | Admin Ver 1.0.0"
admin.site.index_title = "Trivia Chaco 2021 | Admin Dashboard"

from django.contrib import admin
from .models import Trivia, PuntajeUsuario

@admin.register(Trivia)
class TriviaAdmin(admin.ModelAdmin):
    list_display = ["user", "nivel", "fecha"]
    list_filter = ["nivel"]

admin.site.register(PuntajeUsuario)
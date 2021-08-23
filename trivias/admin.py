from django.contrib import admin
from .models import Trivia


@admin.register(Trivia)
class TriviaAdmin(admin.ModelAdmin):
    list_display = ["user", "nivel", "fecha"]
    list_filter = ["nivel"]
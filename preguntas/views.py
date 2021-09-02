from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pregunta, Respuesta

class PreguntaListView(ListView):
    model = Pregunta


class PreguntaDetailView(DetailView):
    model = Pregunta


def preguntadetailrandom(request):
    pregunta = Pregunta.objects.order_by("?").first()
    template = "preguntas/pregunta_detail.html"
    return render(request, template, {"object": pregunta})

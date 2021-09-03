from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pregunta, Respuesta
from trivias.models import PuntajeUsuario

class PreguntaListView(ListView):
    model = Pregunta


class PreguntaDetailView(DetailView):
    model = Pregunta


def preguntadetailrandom(request):
    pregunta = Pregunta.objects.order_by("?").first()
    template = "preguntas/pregunta_detail.html"
    usuario = PuntajeUsuario.objects.filter(usuario = request.user.id).first()
    contexto = {}
    contexto["object"] = pregunta
    contexto["usuario"] = usuario
    return render(request, template, contexto)

def getPreguntasNormal(request):
    context = {}
    preguntas = Pregunta.objects.order_by("?")[:10]
    template = "preguntas/pregunta_listado.html"
    context["object_list"] = preguntas
    return render(request, template, context)

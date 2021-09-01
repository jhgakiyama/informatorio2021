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


def getPreguntasFacil(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=1).order_by("?")[:10]
    template = "preguntas/pregunta_list.html"
    context["object_list"] = preguntas
    context["titulo"] = "(Facil)"
    return render(request, template, context)


def getPreguntasNormal(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=2).order_by("?")[:10]
    template = "preguntas/pregunta_list.html"
    context["object_list"] = preguntas
    context["titulo"] = "(Normal)"
    return render(request, template, context)


def getPreguntasDificil(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=3).order_by("?")[:10]
    template = "preguntas/pregunta_list.html"
    context["object_list"] = preguntas
    context["titulo"] = "(Dificil)"
    return render(request, template, context)



from django.urls import path
from .views import (
    PreguntaListView, PreguntaDetailView, preguntadetailrandom,
    getpreguntasfacil, getreguntasnormal, getpreguntasdificil,
    resultadopregunta
)


urlpatterns = [
    path('', PreguntaListView.as_view(), name='pregunta-list'),
    path('<int:pk>/', PreguntaDetailView.as_view(), name='pregunta-detail'),
    # path('random/', preguntadetailrandom, name='pregunta-detail-random'),
    path('facil/', getpreguntasfacil, name='preguntas-facil'),
    path('normal/', getreguntasnormal, name='preguntas-normal'),
    path('dificil/', getpreguntasdificil, name='preguntas-dificil'),
    path('resultado/', resultadopregunta, name='resultado')
]

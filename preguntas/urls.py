from django.urls import path
from .views import (
    PreguntaListView, PreguntaDetailView, preguntadetailrandom,
    getPreguntasFacil, getPreguntasNormal, getPreguntasDificil
)


urlpatterns = [
    path('', PreguntaListView.as_view(), name='pregunta-list'),
    path('<int:pk>/', PreguntaDetailView.as_view(), name='pregunta-detail'),
    path('random/', preguntadetailrandom, name='pregunta-detail-random'),
    path('facil/', getPreguntasFacil, name='preguntas-facil'),
    path('normal/', getPreguntasNormal, name='preguntas-normal'),
    path('dificil/', getPreguntasDificil, name='preguntas-dificil'),
]

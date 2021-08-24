from django.urls import path
from .views import PreguntaListView, PreguntaDetailView, preguntadetailrandom


urlpatterns = [
    path('', PreguntaListView.as_view(), name='pregunta-list'),
    path('<int:pk>/', PreguntaDetailView.as_view(), name='pregunta-detail'),
    path('random/', preguntadetailrandom, name='pregunta-detail-random')
]

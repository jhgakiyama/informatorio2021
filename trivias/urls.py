from django.urls import path
from .views import TriviaListView, TriviaDetailView


urlpatterns = [
    path('', TriviaListView.as_view(), name='trivia-list'),
    path('<int:pk>/', TriviaDetailView.as_view(), name='trivia-detail')
]

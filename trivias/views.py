from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Trivia


class TriviaListView(ListView):
    model = Trivia


class TriviaDetailView(DetailView):
    model = Trivia

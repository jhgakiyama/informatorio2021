from django.db.models import QuerySet
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.shortcuts import render
from trivias.models import Juego


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = '<strong>Cuenta creada!</strong> Ya puedes iniciar sesión'


class JugarTemplateView(TemplateView):
    template_name = 'jugar.html'


def add(request):
    mi_contexto = {}
    # print("Imprimo claves del POST")
    # for key, value in request.POST.items():
    #     print(f'Key: {key}')
    #     print(f'Value: {value}')
    #
    # print(list(request.POST.items()))
    # print(dict(request.POST.items()))
    #
    # print("Imprimo claves del GET")
    # for key, value in request.GET.items():
    #     print(f'Key: {key}')
    #     print(f'Value: {value}')
    #
    # print(list(request.GET.items()))
    # print(dict(request.GET.items()))

    if request.method == 'GET':
        valor1 = request.GET['num1']
        valor2 = request.GET['num2']
        print("Estoy en el GET")
    else:
        valor1 = request.POST['num1']
        valor2 = request.POST['num2']
        print("Estoy en el POST")

    template = "resultado.html"
    # suma = int(valor1) + int(valor2)

    mi_contexto['num1'] = int(valor1)
    mi_contexto['num2'] = int(valor2)
    return render(request, template_name=template, context=mi_contexto)

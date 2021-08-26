from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserCreationForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = '<strong>Cuenta creada!</strong> Ya puedes iniciar sesión'

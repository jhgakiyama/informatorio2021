"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls
from .views import HomePageView, SignUpView, JugarTemplateView, add
from trivias.views import ranking

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('sumando', add, name='add-name'),
    path('pregunta/', include('preguntas.urls')),
    path('jugar/', JugarTemplateView.as_view(), name='jugar'),
    path('ranking/', ranking, name='ranking')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

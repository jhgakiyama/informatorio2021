from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pregunta, Respuesta
from trivias.models import Juego
from django.contrib.auth.decorators import login_required


class PreguntaListView(ListView):
    model = Pregunta


class PreguntaDetailView(DetailView):
    model = Pregunta


def preguntadetailrandom(request):
    # pregunta = Pregunta.objects.order_by("?").first()
    pregunta = Pregunta.objects.order_by("?")[:10]
    template = "preguntas/pregunta_detail.html"
    return render(request, template, {"object": pregunta})


@login_required
def getpreguntasfacil(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=1).order_by("?")[:10]
    # template = "preguntas/pregunta_list.html"
    template = "preguntas/pregunta_listado.html"
    context["object_list"] = preguntas
    context["nivel"] = "(Facil)"
    return render(request, template, context)


@login_required
def getreguntasnormal(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=2).order_by("?")[:10]
    # preguntas = Pregunta.objects.order_by("?")[:10]
    # preguntas = Pregunta.objects.filter(nivel=2)[:5]
    template = "preguntas/pregunta_listado.html"
    context["object_list"] = preguntas
    context["nivel"] = "(Normal)"
    return render(request, template_name=template, context=context)


@login_required
def getpreguntasdificil(request):
    context = {}
    preguntas = Pregunta.objects.filter(nivel=3).order_by("?")[:10]
    # template = "preguntas/pregunta_list.html"
    template = "preguntas/pregunta_listado.html"
    context["object_list"] = preguntas
    context["nivel"] = "(Dificil)"
    return render(request, template, context)


@login_required
def resultadopregunta(request):
    context = {}
    template = "resultado.html"

    print("Imprimo claves del POST")

    preg_id = []
    dic_p_r = {}
    cont_correcta = 0
    for key, value in request.POST.items():
        # key es la pregunta_id
        # value es la respuesta que se eligio
        if key != 'csrfmiddlewaretoken':
            # print(f'Pregunta_id: {key}')
            # print(f'Rta: {value}')
            rta_selec = Respuesta.objects.get(pk=value)
            llave = int(key)
            dic_p_r[llave] = rta_selec
            preg_id.append(key)
            pregunta = Pregunta.objects.get(pk=key)
            if pregunta.respuesta_es_correcta(int(value)):
                cont_correcta += 1

    # preg_id, es una coleccion de las preguntas_id
    preguntas_originales = Pregunta.objects.filter(pk__in=preg_id)
    dificultad = preguntas_originales[0].nivel
    context['preguntas_originales'] = preguntas_originales
    context['respuestas_sel'] = dic_p_r
    context['correctas'] = cont_correcta

    # creo el nuevo juego
    juego = Juego(
        user=request.user,
        nivel=dificultad,
        puntaje=cont_correcta
    )
    juego.save()
    return render(request, template, context)


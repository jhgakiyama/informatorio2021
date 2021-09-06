from django.shortcuts import render
from django.db.models import Sum
from .models import Juego


def ranking(request):
    template = "ranking.html"
    contexto = {}
    faciles = get_ranking(1)
    normales = get_ranking(2)
    dificiles = get_ranking(3)
    # juegos = Juego.objects.filter(nivel=1).values('user__username').annotate(Sum('puntaje')).order_by('-puntaje__sum')
    # contexto['juegos'] = juegos
    contexto['listado_faciles'] = faciles
    contexto['listado_normales'] = normales
    contexto['listado_dificiles'] = dificiles
    return render(request, template_name=template, context=contexto)


def get_ranking(dif):
    """
    SELECT "username" AS "user__username", SUM("puntaje") AS "puntaje__sum"
    FROM "trivias_juego" INNER JOIN "auth_user" ON (auth_user.id = trivias_juego.user_id)
    where "nivel" = dif
    GROUP BY "user_id"
    ORDER BY "puntaje__sum" DESC

    Juego.objects.filter(nivel=dif).
    values('user__username').
    annotate(Sum('puntaje')).
    order_by('-puntaje__sum')[:5]

    SELECT "username" AS "user__username", SUM("puntaje") AS "puntaje__sum"
    FROM "trivias_juego" INNER JOIN "auth_user" ON (auth_user.id = trivias_juego.user_id)
    where "nivel" = dif
    GROUP BY "user_id" HAVING SUM("puntaje") > 0
    ORDER BY "puntaje__sum" DESC
    """
    return Juego.objects.values('user__username'). \
        annotate(puntaje__sum=Sum('puntaje')). \
        filter(nivel=dif, puntaje__sum__gt=0). \
        order_by('-puntaje__sum')[:10]

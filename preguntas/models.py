from django.db import models
import random

class Pregunta(models.Model):
    CATEGORIA_CHOICES = [
        (1, 'Ciencia y Educación'),
        (2, 'Cultura y arte'),
        (3, 'Deporte'),
        (4, 'Economía'),
        (5, 'Entretenimiento'),
        (6, 'Historia'),
        (7, 'Geografía'),
    ]

    NIVEL_CHOICES = [
        (1, "Facil"),
        (2, "Normal"),
        (3, "Dificil"),
    ]

    texto = models.CharField(max_length=200)
    categoria = models.PositiveSmallIntegerField(
        'categoria',
        choices=CATEGORIA_CHOICES,
        default=6
    )
    nivel = models.PositiveSmallIntegerField(
        'dificultad',
        choices=NIVEL_CHOICES,
        default=2
    )

    def __str__(self):
        return f"{self.texto} ({self.get_nivel_display()})"

    def get_rtas_correctas(self):
        rtas = Respuesta.objects.filter(pregunta=self.id, correcta=True)
        return rtas

    def respuesta_es_correcta(self, rta):
        rtas = self.get_rtas_correctas()
        col_id = []
        for r in rtas:
            col_id.append(r.id)
        if rta in col_id:
            return True
        else:
            return False

    def get_respuestas(self):
        rtas = list(Respuesta.objects.filter(pregunta=self.id))
        random.shuffle(rtas)
        return rtas

    def get_respuestas_ok(self):
        rtas = list(Respuesta.objects.filter(pregunta=self.id, correcta=True))
        # salida = f'{len(rtas)} \n'
        salida = ''
         # en el admin si queda lindo
        # for idx, r in enumerate(rtas, start=1):
        #     salida += f"{idx}){r.texto}.\n"
        # return salida
        for r in rtas:
            salida += f"{r.texto}"
            # salida += f"id: {r.id} - {r.texto}"
        return salida
    get_respuestas_ok.short_description = "Rtas Correctas"

    def get_respuestas_random(self):
        respuestas = list(Respuesta.objects.filter(pregunta=self.id))
        random.shuffle(respuestas)
        return respuestas

    def cant_rtas(self):
        return Respuesta.objects.filter(pregunta=self.id).count()
    cant_rtas.short_description = "Respuestas"

    def cant_rtas_ok(self):
        return Respuesta.objects.filter(pregunta=self.id, correcta=True).count()
    cant_rtas_ok.short_description = "Rtas Correctas"


class Respuesta(models.Model):
    texto = models.CharField(max_length=200)
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name='respuesta'
    )
    correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.texto} (V)" if self.correcta else f"{self.texto} (F)"

    def short(self):
        return f"{self.pregunta.texto[:60]} ..."
    short.short_description = "Pregunta"

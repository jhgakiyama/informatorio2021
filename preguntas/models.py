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

    texto = models.CharField(max_length=200)
    categoria = models.PositiveSmallIntegerField(
        'categoria',
        choices=CATEGORIA_CHOICES,
        default=6
    )

    def __str__(self):
        return f"{self.texto}"

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
    texto = models.CharField(max_length=120)
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name='respuesta'
    )
    correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pregunta: {self.pregunta.texto}, Rta: {self.texto}, Correcta: {self.correcta}"

    def short(self):
        return f"{self.pregunta.texto[:60]} ..."
    short.short_description = "Pregunta"

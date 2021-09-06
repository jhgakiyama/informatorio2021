from django.db import models
from django.contrib.auth.models import User
from preguntas.models import Pregunta
from django.core.validators import MaxValueValidator, MinValueValidator
import random


class Juego(models.Model):
    NIVEL_CHOICES = [
        (1, "Facil"),
        (2, "Normal"),
        (3, "Dificil"),
    ]
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    nivel = models.PositiveSmallIntegerField('dificultad', choices=NIVEL_CHOICES, default=2)
    fecha = models.DateTimeField(auto_now_add=True)
    puntaje = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f"@{self.user} ({self.get_nivel_display()}) | Puntos: {self.puntaje}"


# class Trivia(models.Model):
#     NIVEL_CHOICES = [
#         (1, 'Facil'),
#         (2, 'Normal'),
#         (3, 'Dificil')
#     ]
#
#     nivel = models.PositiveSmallIntegerField(
#         'dificultad',
#         help_text="Nivel de dificultad",
#         choices=NIVEL_CHOICES,
#         default=1
#     )
#     fecha = models.DateTimeField(auto_now_add=True)
#     pregunta = models.ManyToManyField(
#         Pregunta, related_name='trivia_preguntas')
#
#     def __str__(self):
#         return f"#{self.id}| {self.get_nivel_display()}"
#
#     def get_preguntas(self):
#         preguntas = self.pregunta.all()
#         desordenar = list(preguntas)
#         random.shuffle(desordenar)
#         # preguntas = list(Pregunta.objects.filter(id=self.id))
#         # random.shuffle(preguntas)
#         return desordenar
#
#     def cant_preguntas(self):
#         return self.pregunta.all().count()
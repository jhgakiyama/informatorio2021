from django.db import models
from django.contrib.auth.models import User


class Trivia(models.Model):
    NIVEL_CHOICES = [
        (1, 'Facil'),
        (2, 'Normal'),
        (3, 'Dificil')
    ]

    nivel = models.PositiveSmallIntegerField(
        'dificultad',
        help_text="Nivel de dificultad",
        choices=NIVEL_CHOICES,
        default=1
    )

    user = models.ForeignKey(
        'usuario',
        User,
        on_delete=models.CASCADE
    )
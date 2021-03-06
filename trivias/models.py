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
        User,
        related_name='user',
        on_delete=models.CASCADE,
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"@ {self.user}| {self.get_nivel_display()}"

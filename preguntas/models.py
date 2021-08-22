from django.db import models


class Pregunta(models.Model):
    CATEGORIA_CHOICES = [
        (1, 'Cultura y arte'),
        (2, 'Historia'),
        (3, 'Deporte'),
        (4, 'Geografía'),
        (5, 'Economía'),
        (6, 'Ciencia y Educación'),
        (7, 'Entretenimiento')
    ]

    categoria = models.PositiveSmallIntegerField(
        'categoria',
        choices=CATEGORIA_CHOICES,
        default=1
    )

    def __str__(self):
        return str(self.texto)


class Respuesta(models.Model):
    texto = models.CharField(max_length=120)
    correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name='respuesta'
    )

    def __str__(self):
        return f"Pregunta: {self.pregunta.texto}, Rta: {self.texto}, Correcta: {self.correcta}"

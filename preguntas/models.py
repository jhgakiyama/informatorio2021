from django.db import models


class Pregunta(models.Model):
    pass


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

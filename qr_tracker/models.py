from django.db import models

class QRCode(models.Model):
    text = models.CharField(max_length=255)  # Guardará el texto o enlace usado para generar el QR
    generated_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora cuando se generó

    def __str__(self):
        return self.text

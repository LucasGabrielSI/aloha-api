from django.db import models


class Galery(models.Model):
    image = models.FileField(verbose_name='Imagem', upload_to='images_surf/')
    message = models.TextField(verbose_name='Deixe uma mensagem')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'

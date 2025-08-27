from django.db import models
from django.utils import timezone

class Photo(models.Model):
    """Model representing a travel photo."""
    title = models.CharField(max_length=200, verbose_name='Título')
    location = models.CharField(max_length=100, verbose_name='Local')
    description = models.TextField(verbose_name='Descrição')
    date_taken = models.DateField(verbose_name='Data da Viagem')
    image = models.ImageField(upload_to='galeria/images/', verbose_name='Imagem')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-date_taken']
    
    def __str__(self):
        return f"{self.title} - {self.location}"

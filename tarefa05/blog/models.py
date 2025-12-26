# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    
    conteudo = models.TextField(
        verbose_name='Conteúdo'
    )
    
    imagem = models.ImageField(
        upload_to='posts/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )
    
    data_publicacao = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data de Publicação'
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    
    publicado = models.BooleanField(
        default=True,
        verbose_name='Publicado'
    )
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-data_publicacao']
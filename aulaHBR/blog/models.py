from django.db import models
from django.utils import timezone

class Tag(models.Model):
    nome = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.titulo
    
# Para executar, cole este código no shell do Django:
# python manage.py shell

from blog.models import Autor, Post, Tag
from django.utils import timezone
import datetime

# Limpando dados antigos para garantir um ambiente limpo
print("Limpando dados antigos...")
Post.objects.all().delete()
Autor.objects.all().delete()
Tag.objects.all().delete()

# --- Criando Tags ---
print("Criando Tags...")
tag_python = Tag.objects.create(nome='Python')
tag_django = Tag.objects.create(nome='Django')
tag_banco_dados = Tag.objects.create(nome='Banco de Dados')
tag_webdev = Tag.objects.create(nome='WebDev')

# --- Criando Autores ---
print("Criando Autores...")
autor1 = Autor.objects.create(nome='Ana Coder', email='ana.coder@exemplo.com')
autor2 = Autor.objects.create(nome='Bruno Dev', email='bruno.dev@exemplo.com')
autor3 = Autor.objects.create(nome='Carla Sys', email='carla.sys@exemplo.com')

# --- Criando Posts ---
print("Criando Posts...")
# Post 1
post1 = Post.objects.create(
    titulo='Introdução ao Django ORM',
    conteudo='O ORM do Django facilita muito a vida do desenvolvedor...',
    data_publicacao=timezone.make_aware(datetime.datetime(2024, 8, 15)),
    autor=autor1
)
post1.tags.add(tag_django, tag_python, tag_banco_dados)

# Post 2
post2 = Post.objects.create(
    titulo='Consultas Avançadas com Python',
    conteudo='Vamos explorar como fazer consultas complexas.',
    data_publicacao=timezone.make_aware(datetime.datetime(2024, 9, 1)),
    autor=autor2
)
post2.tags.add(tag_python, tag_banco_dados)

# Post 3
post3 = Post.objects.create(
    titulo='Desenvolvimento Web Moderno',
    conteudo='O ecossistema de desenvolvimento web está sempre mudando.',
    data_publicacao=timezone.make_aware(datetime.datetime(2025, 1, 10)),
    autor=autor1
)
post3.tags.add(tag_webdev, tag_django)

# Post 4
post4 = Post.objects.create(
    titulo='Otimizando Queries no Django',
    conteudo='Performance é crucial. Aprenda a usar select_related.',
    data_publicacao=timezone.make_aware(datetime.datetime(2025, 2, 20)),
    autor=autor3
)
post4.tags.add(tag_django, tag_banco_dados)

print("\nBanco de dados populado com sucesso!")

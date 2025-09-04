from aulaHBR.models import Post;

# Exercício 1
Post.objects.filter(autor__nome='Ana Coder', conteudo__icontains='web')

# Exercicio 2

# Execute estes blocos no shell do Django para ver os resultados.
# python manage.py shell

from blog.models import Autor, Post, Tag
from django.db import connection

# ===================================================================
# Slide 10: Criando Dados (Create) [cite: 75]
# ===================================================================
print("\n--- [Slide 10: Create] ---")
# Usando .create() que é a forma mais comum [cite: 82]
novo_autor = Autor.objects.create(nome='Daniel Query', email='daniel.query@exemplo.com')
print(f"Autor criado: {novo_autor.nome}")

post_novo = Post.objects.create(
    titulo='Meu Primeiro Post com ORM',
    conteudo='Este post foi criado diretamente via código Python!',
    autor=novo_autor
)
print(f"Post criado: '{post_novo.titulo}'")

# ===================================================================
# Slide 11: Lendo Dados (Read - all, get) [cite: 90]
# ===================================================================
print("\n--- [Slide 11: Read] ---")
# .all() retorna todos os objetos [cite: 91]
todos_os_posts = Post.objects.all()
print(f"Total de posts na base: {len(todos_os_posts)}")
for post in todos_os_posts:
    print(f" - {post.titulo}")

# .get() retorna um único objeto específico [cite: 92]
try:
    autor_bruno = Autor.objects.get(email='bruno.dev@exemplo.com')
    print(f"\nAutor encontrado com get(): {autor_bruno.nome}")
except Autor.DoesNotExist:
    print("\nAutor não encontrado.")

# ===================================================================
# Slide 12: Filtrando Dados (Read - filter, exclude) [cite: 101]
# ===================================================================
print("\n--- [Slide 12: Filter e Exclude] ---")
# .filter() para encontrar posts que correspondem a um critério [cite: 102]
posts_de_django = Post.objects.filter(titulo__icontains='Django') # icontains é case-insensitive [cite: 113]
print("\nPosts cujo título contém 'Django':")
for post in posts_de_django:
    print(f" - {post.titulo}")

# .exclude() para remover objetos que correspondem a um critério [cite: 103]
posts_sem_ser_da_ana = Post.objects.exclude(autor__nome='Ana Coder')
print("\nPosts que NÃO são da 'Ana Coder':")
for post in posts_sem_ser_da_ana:
    print(f" - '{post.titulo}' por {post.autor.nome}")

# ===================================================================
# Slide 13: Consultas Avançadas com Field Lookups [cite: 110]
# ===================================================================
print("\n--- [Slide 13: Field Lookups] ---")
# Filtrando por ano de publicação [cite: 118]
posts_de_2024 = Post.objects.filter(data_publicacao__year=2024)
print("\nPosts publicados em 2024:")
for post in posts_de_2024:
    print(f" - {post.titulo}")
    
# Filtrando por uma lista de IDs [cite: 116, 119]
autores_especificos = Autor.objects.filter(id__in=[1, 3])
print("\nAutores com ID 1 ou 3:")
for autor in autores_especificos:
    print(f" - {autor.nome}")

# ===================================================================
# Slide 14: Atualizando Dados (Update) [cite: 122]
# ===================================================================
print("\n--- [Slide 14: Update] ---")
# Atualizando um único objeto [cite: 124]
post_para_editar = Post.objects.get(titulo__icontains='Primeiro Post')
print(f"\nTítulo antigo: '{post_para_editar.titulo}'")
post_para_editar.titulo = 'Meu Primeiro Post (Título Atualizado)'
post_para_editar.save()
print(f"Título novo: '{post_para_editar.titulo}'")

# Atualizando múltiplos objetos de uma vez [cite: 128]
num_atualizados = Post.objects.filter(autor__nome='Ana Coder').update(conteudo='[Conteúdo atualizado em massa]')
print(f"\nNúmero de posts da Ana atualizados: {num_atualizados}")


# ===================================================================
# Slide 15: Apagando Dados (Delete) [cite: 132]
# ===================================================================
print("\n--- [Slide 15: Delete] ---")
# Apagando um objeto específico [cite: 134]
post_para_apagar = Post.objects.get(titulo__icontains='Primeiro Post')
print(f"Apagando o post: '{post_para_apagar.titulo}'...")
post_para_apagar.delete()
print("Post apagado.")

# ===================================================================
# Slide 17: Consultas Através de Relacionamentos [cite: 152]
# ===================================================================
print("\n--- [Slide 17: Consultas em Relacionamentos] ---")
# Encontrar posts pelo email do autor [cite: 154]
posts_do_bruno = Post.objects.filter(autor__email='bruno.dev@exemplo.com')
print(f"\nPosts do autor com email 'bruno.dev@exemplo.com':")
for post in posts_do_bruno:
    print(f" - {post.titulo}")

# Encontrar posts pela nome da tag [cite: 156]
posts_com_tag_python = Post.objects.filter(tags__nome='Python')
print("\nPosts com a tag 'Python':")
for post in posts_com_tag_python:
    print(f" - {post.titulo}")

# ===================================================================
# Slide 18: Otimização com select_related [cite: 160]
# ===================================================================
print("\n--- [Slide 18: Otimização] ---")
print("\nIneficiente (N+1 queries):")
# Este loop faz 1 query para buscar todos os posts, e depois
# +1 query para CADA post para buscar o nome do autor. [cite: 164]
for post in Post.objects.all():
    print(f" - '{post.titulo}' por {post.autor.nome}")

print("\nEficiente (select_related - 1 query com JOIN):")
# Este loop faz UMA ÚNICA query ao banco, já trazendo os dados
# do autor junto com os do post usando um JOIN. [cite: 165, 167]
for post in Post.objects.select_related('autor').all():
    print(f" - '{post.titulo}' por {post.autor.nome}")

# ===================================================================
# Slide 19: Usando SQL Puro [cite: 171]
# ===================================================================
print("\n--- [Slide 19: SQL Puro] ---")
def get_primeiro_autor():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nome FROM blog_autor ORDER BY id LIMIT 1")
        row = cursor.fetchone()
    return row[0]

primeiro_autor = get_primeiro_autor()
print(f"O nome do primeiro autor na tabela, via SQL puro, é: {primeiro_autor}")

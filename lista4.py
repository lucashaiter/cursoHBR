'''
# ExAula
carro = {'marca': 'Ford', 'modelo': 'Mustang', 'ano': 2020, 'cor': 'vermelho'}

print(f"\nModelo do carro: {carro.get('modelo')}\n")

carro['quilometragem'] = '10000'
print(f"Quilometragem do carro: {carro['quilometragem']}\n")

for chave, valor in carro.items():
    print(f"{chave.capitalize()} : {valor}")
print("\n")


# ExAula
catalogo = []

livro1 = {'titulo': '1984', 'autor':                            'George Orwell', 'ano': 1949}
livro2 = {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': 1899}

catalogo.append(livro1)
catalogo.append(livro2)

for livro in catalogo:
    print(f"Livro: {livro['titulo']}, por {livro['autor']}, Ano: {livro['ano']}")


# Ex1
aluno = {'nome': 'Lucas', 'idade': '18', 'curso': 'Python'}

aluno['matriculado'] = True

if aluno['matriculado'] == True:
    print(f"O/A {aluno['nome']} está matriculado/a!")
else:
    print(f"O/A {aluno['nome']} não está matriculado/a!")


# Ex2
livro = {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949}

for chave, valor in livro.items():
    print(f"{chave.capitalize()} : {valor}")
'''

# Ex3
estoque = [
    {'nome': 'Caderno', 'preco': 16},
    {'nome': 'Lapis', 'preco': 10}
]

for i in range(len(estoque)):
    for chave, valor in estoque[i].items():
        print(f"{chave.capitalize()} : {valor}")
    print("\n")

'''
# Ex4
coordenadas = (-22.947, -47.149)
print(f"{coordenadas[0]} : Latitude\n{coordenadas[1]} : Longitude")


# Ex5
localizacao = {'cidade': 'Campinas', 'coordenadas': (-22.910, -47.068)}

print(f"A cidade {localizacao['cidade']} tem latitude {localizacao['coordenadas'][0]}")
'''
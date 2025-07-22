'''
# ExAula
def gerar_cabecalho(titulo, autor="Equipe de Dados"):
    return f"--- {titulo} ---\nAutor: {autor}"

cab1 = gerar_cabecalho("Lucas")
print(cab1)
cab2 = gerar_cabecalho(titulo="Livro das trevas", autor="Lucas TI")
print(cab2)


# ExAula2
def montar_relatorio(titulo, *metricas, **informacoes_extras):
    print(f"--- {titulo} ---")

    print("\n-- Métricas: ")
    for metrica in metricas:
        print(f"{metrica}")

    print("\n-- Informações extras: ")
    for chave, valor in informacoes_extras.items():
        print(f"{chave.capitalize()}: {valor}")

montar_relatorio("Relatório de Vendas", "Total: R$50.000", "Itens vendidos: 800", data="18/06/2025", gerente="Sra. Silva")


# Ex1
mensagem = "Olá, mundo!"
def modificar_mensagem():
    mensagem = "Olá do escopo local!"
    print("Dentro da função:", mensagem)

modificar_mensagem()
print("Fora da função:", mensagem)

# O valor da variável 'mensagem' não foi alterado fora da função pois foi definido uma outra variável 
# com mesmo nome porém dentro da função 'modificar_mensagem()', ou seja, mesmo tendo nomes iguais, 
# são escopos diferentes, quer dizer que a variável 'mensagem' do escopo global, não foi modificada após a entrada na função


# Ex2
contador = 0

def incrementar(cont):
    return cont + 1

contador = incrementar(contador) # 1
contador = incrementar(contador) # 2

print(contador)


# Ex3
def exibir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome.capitalize()}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade.capitalize()}")

exibir_informacoes(nome="lucas", idade=18, cidade="campinas")


# Ex4
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

total1 = soma(1, 6, 8, 9, 1, 4) 
print(f"A soma dos números 1, 6, 8, 9, 1, 4 é de: {total1}")
total2 = soma(30, 60, 80, 20) 
print(f"A soma dos números 30, 60, 80, 20 é de: {total2}")
'''

# Ex5
def exibir_usuario(**info):
    print("-- Informações --")
    for chave, valor in info.items():
        print(f"{chave.capitalize()}: {valor}")

exibir_usuario(nome="Alice", idade=25, profissao="Engenharia")
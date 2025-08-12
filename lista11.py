'''
# Aula
with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira vez!\n")

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Olá mundo!\n")

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(f"{linha.strip()}")


# Aula
try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos")
except:
    print("Erro! Você não digitou um número válido!")

# Aula
while True:
    try:
        num = int(input("Digite um número: "))
        resultado = 10 / num
        print(f"O resultado é {resultado}")
        break
    except Exception as e:
        print(f"Ocorreu um erro inesperado! {e}")


# ExAula
from datetime import datetime
while True:
    try:
        mensagem = input("Digite uma mensagem: ")
        with open("log.txt", "a") as arquivo:
            data = datetime.now().strftime("%d-%m-%Y - %H:%M:%S")
            arquivo.write(f"{data} - {mensagem}\n")
        break
    except Exception as e:
        print(f"\nErro! {e}\n")
        
try:
    with open("config.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)
except Exception as e:
    print(f"Arquivo de configuração não encontrado, usando padrões! {e}")


# Ex1
try:
    usuario = input("Digite seu nome de usuário: ")
    with open("usuario.txt", "w") as arquivo:
        arquivo.write(usuario)
except Exception as e:
    print(f"Erro: {e}")


# Ex2
try:
    with open("usuario.txt", "r") as arquivo:
        nome = arquivo.readlines()
    print(f"Bem vindo {nome[0]}!")
except Exception as e:
    print(f"Erro: {e}")


# Ex3
from datetime import datetime
evento = input(f"Informe um evento: ")
with open("log.txt", "a") as arquivo:
    data = datetime.now().strftime("%d-%m-%Y - %H:%M:%S")
    arquivo.write(f"{evento} - {data}")


# Ex4
total = 0
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        try:
            n = float(linha)
            total += n
        except Exception as e:
            print(f"Erro: ({e}) - na linha ({linha.strip()})")
print(f"Total: {total}")
'''

# Ex5
nome = input("Digite o nome do produto: ")

try:
    quantidade = int(input("Digite a quantidade do produto: "))
except ValueError as e:
    print(f"Erro - ({e})")

try:
    precoUnit = float(input("Digite o preço unitário do produto: "))
except ValueError as e:
    print(f"Erro - ({e})")

with open("produtos.txt", "a") as arquivo:
    arquivo.write(f"{nome} - {quantidade} unidade(s) - R${precoUnit}\n")
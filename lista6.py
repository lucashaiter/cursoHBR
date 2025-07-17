'''
# Ex1
def saudacao(nome):
    print(f"---------- Bem vindo {nome}! ----------")

saudacao("Lucas")
saudacao("Danilo")
'''
#------------------------------------------------------------

# Ex2
import os
def limpar_terminal():
  """Limpa o terminal, independente do sistema operacional."""
  os.system('cls' if os.name == 'nt' else 'clear')


def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro! Denominador igual a 0!"
    else: 
        return n1 / n2

def mostrarMenu():
    opcao = input("Digite a operação que deseja realizar!\n1 - Soma\n2 - Subtração\n3 - Multiplição\n4 - Divisão\n\n")
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        return soma(num1, num2)
    elif opcao == "2":
        return subtracao(num1, num2)
    elif opcao == "3":
        return multiplicacao(num1, num2)
    elif opcao == "4":
        return divisao(num1, num2)
    else:
        return "Operação inválida!"
    
continuar = "S"
while True:
    if continuar.upper() == "S":
        valor = mostrarMenu()
        limpar_terminal()
        print(f"O valor foi de: {valor}")
        continuar = input("Deseja continuar! (S/N): ")
    else:
        print("Programa finalizado!")
        break

#------------------------------------------------------------
'''
# Ex3
def maiorIdade(idade):
    if idade >= 18:
        return True
    else:
        return False

idade = int(input("Digite sua idade: "))
resultado = maiorIdade(idade)

if resultado == True:
    print("Acesso permitido!")
else:
    print("Acesso Negado!")

#------------------------------------------------------------

# Ex4
def calcularArea(largura, altura):
    return largura * altura

lq = float(input("Digite a largura do quarto: "))
aq = float(input("Digite a altura do quarto: "))
print(f"A área do quarto é de: {calcularArea(lq, aq)} m²\n")

lc = float(input("Digite a largura do cozinha: "))
ac = float(input("Digite a largura do cozinha: "))
print(f"A área da cozinha é de: {calcularArea(lc, ac)} m²")

#------------------------------------------------------------


# Ex5
from django.shortcuts import render

def pagina_inicial(request):
    context = {'titulo': 'index'}
    return render(request, 'index.html', context)

pagina_inicial()
'''
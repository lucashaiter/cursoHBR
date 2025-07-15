'''
#ExAula
senhaCorreta = "python123"
senha = ""
while True:
    senha = input("Digite a senha correta: ")

    if senha == senhaCorreta:
        break
    else:
        print("Senha incorreta!\n")
print("Acesso permitido!")


#ExAula
import random
numeroCorreto = random.randint(1, 100)
numero = 0
cont = 0
print("-------Jogo da Adivinhação-------")
while True:
    numero = int(input("Digite um número: "))
    cont += 1

    if numero > numeroCorreto:
        print("Muito alto!\n")
    elif numero < numeroCorreto:
        print("Muito baixo!\n")
    else:
        print(f"\nVocê acertou!\nVoce utilizou de {cont} tentativa(s)!")
        break


# Ex1
opcao = ""
usuarios = []
while opcao != "3":
    print("\nMenu Interativo\n1 - Listar usuário\n2 - Cadastrar Usuário\n3 - Sair")
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        for i in range(len(usuarios)):
            print(f"{usuarios[i]}")
    elif opcao == "2":
        usuarios.append(input("Digite seu nome de usuário: "))
print("\n\nPrograma finalizado!")

# Ex2
usuarioCorreto = "lucashaiter"
senhaCorreto = "12345678"
cont = 0
print("----------Sistema de login----------")
while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    cont += 1

    if cont < 3:
        if usuario != usuarioCorreto:
            print("Usuário incorreto!")
        elif senha != senhaCorreto:
            print("Senha incorreta!")
        else:
            print("Logado!")
            break
    else:
        print("Excedeu o limite de tentativas!")
        break        

# Ex3
usuarios = ["user", "guest", "admin"]
print("Verificação de usuário!")
cont = 0
while cont <= len(usuarios):
    if usuarios[cont] != "admin":
        print(f"'{usuarios[cont]}' não é 'admin'!")
        cont += 1
        continue
    else:
        print(f"Achou o '{usuarios[cont]}'")
        break
print("Programa finalizado!")
'''
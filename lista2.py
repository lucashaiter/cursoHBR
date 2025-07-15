# Ex Aula
senhaCorreta = "12345"
usuarioCorreto = "admin"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuarioCorreto and senha == senhaCorreta:
    print("Login bem-sucedido")
elif usuario != usuarioCorreto and senha == senhaCorreta:
    print("Usuário inválido")
elif usuario == usuarioCorreto and senha != senhaCorreta:
    print("Senha inválida")
else:
    print("Usuário e senha não encontrados")


# Ex1
nome = input("Digite seu nome completo: ")
cidade = input("Onde você mora: ")

nomeMaisuculo = nome.strip().upper()
print(f"Nome completo em maiusculo: {nomeMaisuculo}")

nomeMinusculo = nome.strip().lower()
print(f"Nome completo em minusculo: {nomeMinusculo}")

cidadeLetraMaiu = cidade.strip().capitalize()
cidadeLetraMaiu = cidade.replace(" ", "")
print(f"Cidade com a primeira letra maiúscula: {cidadeLetraMaiu}")

nome = nome.replace(" ", "")
print(f"O numero de letras no nome é: {len(nome.strip(  ))}")


# Ex2
idade = int(input("Qual sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente")
else:
    print("Você é um adulto")


# Ex3
pontuacaoCredito = int(input("Digite sua pontuação de crédito: "))
rendaMensal = float(input("Digite sua renda mensal: "))

if pontuacaoCredito > 600 and rendaMensal >= 2500.00:
    print("Aprovado")
else:
    print("Recusado") 


# Ex4
convite = input("Digite o tipo do convite: ")
idade = int(input("Digite sua idade: "))

if convite.upper() == "VIP" or idade >= 18:
    print("Liberado")
else:
    print("Negado")


# Ex5
senha = input("Digite sua senha: ")
confirmaSenha = input("Confirme sua senha: ")

if senha != confirmaSenha:
    print("Inválido!")
elif senha == "12345":
    print("Não é possível utilizar senha antiga!")    
elif len(senha) < 8:
    print("Menos que 8 caracteres!")
else:
    print("Nova senha confirmada!")
    
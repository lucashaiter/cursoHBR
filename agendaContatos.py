import os
def limparTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------

# Lista com todos os contatos
listaContatos = []

# Classe Contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

# Função para voltar ao menu
def voltarMenu():
    input("\nDigite qualquer coisa para voltar ao menu ...")
    limparTerminal()

def buscarPor(escolha):
    print(f"-------------------------- Procurar pelo {escolha.upper()} --------------------------")
    nomeProcura = input(f"Digite o {escolha.upper()} EXATAMENTE como foi salvo: ")
    encontrado = False
    for contato in listaContatos:
        if contato[f'{escolha}'] == nomeProcura:
            print(f"\nInformações encontradas com o {escolha.upper()}:\n" \
            f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
            encontrado = True
    if encontrado == False:
        print("\nNada encontrado!\n")
        voltarMenu()
    else:
        voltarMenu()

# Função para adicionar contato
def adicionarContato():
    nome = input("Nome do Contato: ")
    telefone = input("Telefone do Contato: ")
    email = input("Email do contato: ")
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    listaContatos.append(contato)
    print("\n-------------------------- Contato adicionado! --------------------------\n")
    voltarMenu()

# Função para listar contato
def listarContato():
    for contato in listaContatos:
        print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    print("\n---------------------------------------------------------------------\n")
    voltarMenu()

# Função para buscar contato
def buscarContato():
    escolha = input("Você deseja procurar pelo:\n" 
    "1. Nome\n" 
    "2. Telefone\n" 
    "3. Email\n"
    "Opção: ")

    if escolha == "1":

        limparTerminal()
        buscarPor("nome")

    elif escolha == "2":

        limparTerminal()
        buscarPor("telefone")

    elif escolha == "3":

        limparTerminal()
        buscarPor("email")

    else:
        print("Opção inválida!\n")
        voltarMenu()


# Função para remover contato
def removerContato():
    nomeRemover = input("Digite o NOME do contato que você deseja remover: ")
    for contato in listaContatos:
        if contato['nome'] == nomeRemover:
            print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
            opcao = input("Deseja remover? (S/N): ")

            if opcao.upper() == "S":

                listaContatos.remove({'nome': contato['nome'], 'telefone': contato['telefone'], 'email': contato['email']})
                print("Nome removido!\n")
                voltarMenu()

            elif opcao.upper() == "N":

                voltarMenu()

            else:

                print("Opção inválida!\n")
                voltarMenu()

    print("Não encontrado!\n")
    voltarMenu()


# Menu principal
def menuPrincipal():
    print(
    "-------------------------- Agenda de Contatos --------------------------\n" 
    "-                        1. Adicionar contato                          -\n" 
    "-                        2. Listar contatos                            -\n"
    "-                        3. Buscar contato                             -\n"
    "-                        4. Remover contatos                           -\n"
    "-                        5. Sair                                       -\n"
    "------------------------------------------------------------------------")

    opcao = input("Digite a opção: ")

    if opcao == "1":

        limparTerminal()
        print("-------------------------- Adicionar Contato --------------------------")
        adicionarContato()

    elif opcao == "2":

        limparTerminal()
        print("-------------------------- Listar Contatos --------------------------")
        listarContato()

    elif opcao == "3":

        limparTerminal()
        print("-------------------------- Buscar Contato --------------------------")
        buscarContato()

    elif opcao == "4":

        limparTerminal()
        print("-------------------------- Remover Contato --------------------------")
        removerContato()

    elif opcao == "5":

        limparTerminal()
        print("\nPrograma Finalizado!")

    else:
        print("\nOpção Inválida!")
        voltarMenu()


# --------------------------------------------------------

# Chamada do menu principal
if __name__ == "__main__":
    while True:
        menuPrincipal()

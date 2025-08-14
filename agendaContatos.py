# Import da bibliotecas
import os
import json

# Função para limpar o terminal
def limparTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------

# Função para adicionar contato
def adicionarContato():
    listaContatos = []

    nome = input("Nome do Contato: ")
    telefone = input("Telefone do Contato: ")
    email = input("Email do contato: ")
    contato = {'nome': nome, 'telefone': telefone, 'email': email}

    try:
        with open("arquivoContatos.json", "r") as arquivoContatos:
            listaContatos = json.load(arquivoContatos)

    except FileNotFoundError:
        pass

    confirmar = input("Voce deseja adicionar esse contato? (S/N): ")

    if confirmar.upper() == "S":
        listaContatos.append(contato)

        try:
            with open("arquivoContatos.json", "w", encoding="utf-8") as arquivoContatos:
                json.dump(listaContatos, arquivoContatos, indent=4, ensure_ascii=False)
                print("\n-------------------------- Contato adicionado! --------------------------\n")

        except Exception as e:
            print(f"\nErro! - {e}\n")
            pass

    else:
        print("\n-------------------------- Processo Negado! --------------------------\n")
    
    voltarMenu()

# ----------------------------------------------------------------------------------------------------------------

# Função para listar contato
def listarContato():
    listaContatos = []
    try:
        with open("arquivoContatos.json", "r") as arquivoContatos:
            listaContatos = json.load(arquivoContatos)
        
        if len(listaContatos) == 0:
            print("Lista vazia!")
        else:
            for contato in listaContatos:
                print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    except FileNotFoundError:
        print(f"Lista vazia!")

    print("\n---------------------------------------------------------------------\n")
    voltarMenu()

# ----------------------------------------------------------------------------------------------------------------

# Função para buscar contato
def buscarPor(escolha):
    listaContatos = []
    print(f"-------------------------- Procurar pelo {escolha.upper()} --------------------------")

    nomeProcura = input(f"Digite o {escolha.upper()} EXATAMENTE como foi salvo: ")
    encontrado = False

    try:
        with open("arquivoContatos.json", "r") as arquivoContatos:
            listaContatos = json.load(arquivoContatos)

            for contato in listaContatos:
                if contato[f'{escolha}'] == nomeProcura:
                    print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
                    encontrado = True
            
            if encontrado == False:
                print("\nNada encontrado na lista!\n")

    except FileNotFoundError:
        print(f"Nada encontrado na lista!")

    voltarMenu()

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

# ----------------------------------------------------------------------------------------------------------------

# Função para remover contato
def removerContato():
    listaContatos = []
    i = 1

    try:
        with open("arquivoContatos.json", "r") as arquivoContatos:
            listaContatos = json.load(arquivoContatos)

    except FileNotFoundError:
        pass

    if len(listaContatos) == 0:
        print("Lista vazia!\n")

    else:
        for contato in listaContatos:
            print(f"{i}: {contato['nome']} - {contato['telefone']} - {contato['email']}")
            i += 1

        indiceRemover = input("\nDigite o Indíce do contato que você deseja remover: ")

        if len(indiceRemover) == 0:
            print("Número inválido!\n")

        else:
            if int(indiceRemover) > len(listaContatos):
                print("Número inválido!\n")
            
            else:
                listaContatos.pop(int(indiceRemover) - 1)
                
                try:
                    with open("arquivoContatos.json", "w", encoding="utf-8") as arquivoContatos:
                        json.dump(listaContatos, arquivoContatos, indent=4, ensure_ascii=False)
                    print("\nNome Removido!")

                except Exception as e:
                    print("\nErro - {e}")
        
    voltarMenu()


# ----------------------------------------------------------------------------------------------------------------

# Menu principal
def menuPrincipal():
    continuar = True
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
        continuar = False

    else:
        print("\nOpção Inválida!")
        voltarMenu()

    return continuar

# ----------------------------------------------------------------------------------------------------------------

# Chamada do menu principal
if __name__ == "__main__":
    while True:
        limparTerminal()
        if menuPrincipal() == False:
            break

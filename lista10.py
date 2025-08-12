'''
# ExAula
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self, quantidade):
        if quantidade <= self.estoque and quantidade > 0:
            self.estoque = self.estoque - quantidade
            print(f"Vendido {quantidade} unidades de {self.nome}!")
        else:
            print("Estoque inválido!")

    def exibirEstoque(self):
        print(f"Estoque - {self.estoque}")

sorvete = Produto("Flocos", 19, 30)
print(f"{sorvete.nome} - R${sorvete.preco}")
sorvete.exibirEstoque()
sorvete.vender(18)
sorvete.exibirEstoque()
sorvete.vender(90)
sorvete.exibirEstoque()


# ExAula
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibirDados(self):
        print(f"{self.nome} - R${self.salario:.2f}")
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor
    
    def exibirDados(self):
        print(f"{self.nome} - R${self.salario:.2f} - Setor da {self.setor}")

junior = Funcionario("Junior", 22900)
julia = Gerente("Julia", 43900, "Computação")

junior.exibirDados()
julia.exibirDados()


# Ex1
class Animal:
    def falar(self):
        return "Olá"

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau Miau"

person = Animal()
dog = Cachorro()
cat = Gato()

person.falar()
dog.falar()
cat.falar()


# Ex2
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

pessoa = Pessoa("Lucas")
print(f"{pessoa.nome}")

professor = Professor("Danilo", "Geografia")
print(f"{professor.nome} - {professor.disciplina}")


# Ex3
class Animal:
    def falar(self):
        return "Olá"

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau Miau"

def apresentar(animal):
    print(animal.falar())

person = Animal()
dog = Cachorro()
cat = Gato()

apresentar(person)
apresentar(dog)
apresentar(cat)
'''

# Ex4
# Não entendi

# Ex5
class Falante:
    def acao(self):
        return "Fala!"

class Andador:
    def acao(self):
        return "Anda!"
    
class Pessoa(Falante, Andador):
    def acao(self):
        return f"{Falante.acao(self)} e {Andador.acao(self)}"
    
pessoa = Pessoa()
print(pessoa.acao())
    
        
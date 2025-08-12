'''
# Ex1
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

meuDog = Cachorro("Tufo", 18)
print(f"O {meuDog.nome} tem {meuDog.idade} anos!")

# Ex2
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"Au Au {self.nome}!") 

meuDog = Cachorro("Tufo", 18)
meuDog.latir()

# Ex3
class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

livro1 = Livro("Bibllia Sagrada", "Wesley Safadão")
livro2 = Livro("FNAF", "Junior Arroba")
print(f"O livro {livro1.titulo} foi escrito pelo {livro1.autor}, já o livro {livro2.titulo} foi escrito pelo {livro2.autor}!")
'''

# Ex4
class Retangulo:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def areaRetangulo(self):
        area = self.largura * self.comprimento
        return area

    def perimetroRetangulo(self):
        perimetro = 2 * (self.largura + self.comprimento)
        return perimetro
    
desenho = Retangulo(7, 8)
print(f"O desenho real possui: {desenho.areaRetangulo()} m² de área!")
print(f"O desenho possui {desenho.perimetroRetangulo()} m de perímetro!")


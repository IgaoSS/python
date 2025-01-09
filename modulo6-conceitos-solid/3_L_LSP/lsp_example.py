class Animal:
    def comer(self):
        print("O animal está comendo")

    def andar(self):
        print("O animal está andando")

class Felino(Animal):
    def lamber(self):
        print("O felino está lambendo seu pelo")

    # Esse override é uma quebra do princípio de Liskov
    '''
    def comer(self):
        print("O felino com sua ração")
    '''

class Leao(Felino):
    def rugir(self):
        print("O leão está rugindo alto!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

animal = Animal()
felino = Felino()
leao = Leao()
pessoa = Pessoa()

# Esse é o princípio de substituição de Liskov, usando o tipo ou subtipo (classe ou classe herdada), o comportamento se mantém o mesmo
pessoa.observa(animal)
pessoa.observa(felino)
pessoa.observa(leao)
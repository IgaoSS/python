# Super - chama a implementação padrão da classe mâe
# Executa o que a classe mãe faz e depois o que o usuário passar para ser executado

'''
super().emitir_som()
return "Morcegos emitem sons ultrassônicos"
'''

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

#Acessando os métodos da classe mãe [Animal]
print(f"Nome do morcego: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

#Acessando os métodos das classes [Mamíferos e Aves]
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")
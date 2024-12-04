# Herança, Polimorfismo e Encapsulamento


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

# Polimorfismo: usar o mesmo método definido na classe mãe, mas de uma forma atualizada para a classe específica
# Classe mãe tem o método emitir_som mas de maneira padrão
# A classe Cachorro e Gato reescreveram o método com implementações diferentes, cada um com seu respectivo som

print("\nExemplo de herança:")

# Exemplo de Herança
# Permitir que uma classe extenda as propriedades e métodos de uma classe mãe

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
dog = Cachorro("Rex")
cat = Gato("Felix")

print("\nExemplo de polimorfismo:")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

# Encapsulamento
# Proteger os dados dentro da classe, para evitar de ser usado de maneira errônea em lugares indevidos
print("\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo Privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
print(f"Saldo da conta bancária 1: {conta.consultar_saldo()}")

conta.depositar(500)
print(f"Saldo da conta bancária 1: {conta.consultar_saldo()}")

conta.sacar(250)
print(f"Saldo da conta bancária 1: {conta.consultar_saldo()}")

conta2 = ContaBancaria(50)
print(f"Saldo da conta bancária 2: {conta2.consultar_saldo()}")


# Abstração
# Serve apenas como um molde
#Serve como um contrato/interface

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    #Decorador - definir que essa é uma classe abstrata
    #Definindo que quando for derivar essa classe, o método ligar é obrigatório ser definido o que ele vai fazer
    #Não se cria implementação nos métodos abstratos

    @abstractmethod 
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo =  Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
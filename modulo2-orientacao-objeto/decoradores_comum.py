# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome):
        self.nome = nome # Atributo de instância

    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    # Permite acessar o método sem precisar instanciar um ojbeto
    # Recebe a referência da classe como parâmetro, usa o cls como self
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor={cls.valor}"
    
    # Não recebe a referência da classe como parâmetro
    # Ele faz parte da classe, mas não tem acesso nem à classe(cls), nem a instância(self)
    # Não pode modificar o estado da instância do objeto nem o estado da classe
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"


obj = MinhaClasse("Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

# Exemplo de ClassMethod
print("\nExemplo de ClassMethod")
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nMarca: {carro1.ano}")

# Exemplo de StaticMethod
print("\nExemplo de StaticMethod")
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))
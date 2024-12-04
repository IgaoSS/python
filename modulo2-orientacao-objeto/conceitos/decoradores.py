#Adicionar funcionalidades a métodos que não necessariamente a gente precisar alterar o código original dessa função
#Tipo especial de função que vai permitir modificar ou extender comportamentos de outras funções

#Decoradores são bastate utilizados em validações
#Exemplo: Antes de já logar o user no sistema, verifica se ele possui cadastro

#Wrapper = é um tipo de embrulho, algo que fica envolta da função

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")

    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

print("")

# Decorador em classe
class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    # __call__ precisa desse método para ser executado quando a classe é usada como decorador
    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()
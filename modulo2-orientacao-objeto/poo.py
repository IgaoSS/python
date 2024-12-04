# Classe exemplo
class Pessoa:
    # Construtor da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

#Objetos
pessoa1 = Pessoa("Igor", 23)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Sabrina", 21)
mensagem = pessoa2.saudacao()
print(mensagem)


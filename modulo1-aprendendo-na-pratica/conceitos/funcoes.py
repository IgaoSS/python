# Exemplo de função

def saudacao(nome):
    print(f"Olá, {nome}!")

print("Chamando a função saudação: ")
saudacao("Igor")
saudacao("João")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando a função quadrado:")
print(f"O quadrado de 5 é {quadrado(5)}")

# Função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função de soma:")
numero1 = 45
numero2 = 67
print(f"A soma de {numero1} + {numero2} = {soma(numero1, numero2)}")

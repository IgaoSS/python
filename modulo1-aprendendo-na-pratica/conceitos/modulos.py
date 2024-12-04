# Blocos de código que podem ser reutilizados em outros arquivos

print("Exemplo de importação de módulo padrão:")

# Importando tudo 
# import math

# Importando apenas o que será utilizado
from math import sqrt

numero = 144
raiz_quadrada = sqrt(numero)
print(f"A raiz quadrada de {numero} é {int(raiz_quadrada)}")

print("\nExemplo de criação e utilização de um módulo personalizado")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Igor")
resultado_dobro = dobro(23)

print(mensagem)
print(resultado_dobro)
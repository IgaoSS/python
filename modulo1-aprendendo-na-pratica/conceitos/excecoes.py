print("Exemplo de captura de exceções")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10/numero
# Erro de valor
except ValueError as e:
    print(f"Erro de valor: {e}")
    raise ValueError("Tipo de variaveis incompatíveis")
# Erro de exceção genérico
except Exception as e:
    print(f"Erro: {e}")
# Executa se deu certo
else:
    print(resultado)
# Executa mesmo se deu certo ou errado
finally:
    print("Operação finalizada")
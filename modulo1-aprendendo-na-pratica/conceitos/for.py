# Lista
print("\nFor usando um dicionário")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Tuplas
print("\nFor usando uma tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

# Dicionário
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Chaves
print("\nFor utilizando dicionário - chaves")
for chave in pessoa.keys():
    print(chave)

# Valores
print("\nFor utilizando dicionário - valores")
for chave in pessoa.keys():
    print(chave)

# Itens
print("\nFor utilizando dicionário - itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Método range: intervalo numérico
print("\nUtilizando a função range()")
for numero in range(8):
    print("Número:", numero)

# Método len
print("\nUtilizando a função range() com len()")
for indice in range(0, len(lista)):
    print(f"Indice[{indice}]: {lista[indice]}")

# Método Enumerate: extrai a informação do valor e do indice
print("\nUtilizando a função enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Indice: {indice}, Valor: {valor}")
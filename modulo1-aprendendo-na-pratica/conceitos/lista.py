minha_lista = [10, 20, 30, 40, 50, 60, 70, 80]

# Exibindo a lista por completo
print("Minha lista de exemplo: ", minha_lista)

# Exibindo os elementos da lista de forma individual
print("Minha lista na posição 0: ", minha_lista[0])

# O primeiro é o índice origem, e tem que ser até o indice alvo + 1
# Exemplo: na lista o [6] é o True, mas preciso colocar 7
print(minha_lista[1:7])

# Alvo + 1, para ir do início até um alvo final
# Vai ir até o rocketseat
print(minha_lista[:6])

# A partir do meu segundo indice, pega tudo pra frente
print(minha_lista[2:])

# Substituindo o valor de um elemento da lista
print("Minha lista antes da alteracao: ", minha_lista)
minha_lista[0] = 100
print("Minha lista depois da alteracao: ", minha_lista)

# ----------- Métodos de lista -----------

# Método append: add um item no final da lista
minha_lista.append(60)
print("MInha lista apos adicionar com append: ", minha_lista)

# Método Index: retornar o index de um item específico
indice = minha_lista.index(60)
print("Indice do elemento 64: ", indice)

# Método insert: insere um elemento em um indice especifico
# Caso exista um elemento no indice especificado, ele entrará no lugar e empurrará os demais para frente
minha_lista.insert(2, 90)
print("Minha lista apos adicionar com insert: ", minha_lista)

# Método pop: Deleta o elemento de um índice específico
# Necessário +1, quero remover o elemento do indice 2, tenho que passar 3
# Ele remove e retorna o elemento removido da lista
elemento_removido = minha_lista.pop(3)
print("Elemento removido: ", elemento_removido)
print("Lista apos o pop(3):", minha_lista)

# Método remove: remove um elemento especifico
# Ele remove o primeiro elemento encontrado, caso exista mais de um, ele remove apenas o primeiro
minha_lista.remove(60)
print("Minha lista apos remover: ", minha_lista)

# Método sort: organizar a lista em ordem crescente
# Tem que ser o mesmo tipo de dado
minha_lista.sort()
print("Minha lista apos sort: ", minha_lista)
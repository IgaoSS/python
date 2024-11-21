# Coleção ordenada e imutável de elementos
# Depois de declarada, não pode ser alterada

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla: ", minha_tupla)

# Acessando o elemento
print("Elemento na posição 2: ", minha_tupla[2])

# Acessando o último elemento
print("Elemento na útlima posição: ", minha_tupla[-1])

# ------------ Métodos ------------

# Méotodo count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece: ", contagem)

# Método index
indice = minha_tupla.index(3)
print("Índice da primeira ocorrência do meu elemento 3: ", indice)
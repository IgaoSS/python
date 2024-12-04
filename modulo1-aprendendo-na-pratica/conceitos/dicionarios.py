# Coleção não ordenada de pares chave-valor

# Criando um dicionário de exemplo
pessoa = {
    "nome": "Igor",
    "idade": 23,
    "cidade": "São Paulo"
}

print("Meu dicionário: ", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando uma nova chave ao dicionário
pessoa["sobrenome"] = "Sousa"
print("Meu dicionário atualizado: ", pessoa)
print("Sobrenome:", pessoa["sobrenome"])

# ----------- Métodos -----------

# Atualizando um valor do dicionário
pessoa["idade"] = 25
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário após remoção: ", pessoa)

# Método keys(): Retorna todas as chaves que tem no dicionário (Nome, Idade, Cidade, ....)
chaves = pessoa.keys()
print("Chaves do dicionário: ", chaves)
print("Chaves do dicionário em formato de lista: ", list(chaves))

# Método values: Retorna todos os valores que tem no dicionário
valores = pessoa.values()
print("Valores do dicionário: ", valores)
print("Valores do dicionário em formato de lista: ", list(valores))

# Método items: Retorna todos os pares presentes no dicionário em formato de tupla
itens = pessoa.items()
itens_format_list = list(pessoa.items())
print("Pares chave-valor do dicionário: ", itens)
print("Retornando a primeira tupla: ", itens_format_list[0])
print("Retornando o primeiro elemento da primeira tupla: ", itens_format_list[0][1])
nome = "Igor Sousa da Silva"
telefone = "(11) 96739-5427"
texto = "xIgorx"

#Métodos do tipo texto
print(f"Nome em maiúsculo: {nome.upper()}")
print(f"Nome em minúsculo: {nome.lower()}")
print(f"Quantidade de letras A em [{nome}]: {nome.count('a')}")

#Tamanho de uma string
print(f"Quantidade de caracteres em [{nome}]: {len(nome)}")

#Encontrar index do caracter
print(f"Encontrando a posição da primeira letra O em [{nome}]: {nome.find('o')}")

#Função para fazer conversão de bytes
print(nome.encode())
print(nome.encode().decode())

#Replace
print(telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

#Join - Cada caractere é separado por alguma coisa
print("-".join("Igor"))

#Split - Transforma em um array
print(nome.split(" "))

#Strip - remove tudo que bate com meu alvo e que está no começo ou fim da minha string
print(texto.strip("x"))

#rstrip - remove tudo que bate com meu alvo e que está na direita
print(texto.rstrip("x"))

#startwith - verifica se a string começa com algo
print(nome.startswith("Ig"))

# in - Verifica se existe uma ocorrência dentro de uma string
print("da" in nome)

# not in - Contrário do in, se nao tiver, é verdadeiro (da nao existe em Igor Sousa da Silva)
print("xg" not in nome)
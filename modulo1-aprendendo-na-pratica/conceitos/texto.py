# Declaração
nome_completo = "Igor Sousa"

nome_completo_aspas= """Igor
Sousa"""

# Mesma coisa quando escreve tudo na mesma linha
# Serve apenas para caso queira deixa com uma estética mais agradável textos grandes
nome_completo_quebra = "Igor \
Sousa"

nome = "Igor"
sobrenome = "Sousa"

#Formatação
print("Nome completo (1ª forma):", nome_completo)
print("Nome completo (2ª forma):" + nome_completo)
print("Nome completo (3ª forma):" + "Igor" + "Sousa")
print("Nome completo (4ª forma):" + "Igor", "Sousa")
print("Nome completo (5ª forma):", nome_completo_aspas)
print("Nome completo (6ª forma):", nome_completo_quebra)
print("Nome completo (7ª forma): %s" % nome_completo)
print("Nome completo (8ª forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª forma): {nome} {sobrenome}")
print("Nome completo (10ª forma): {} {}".format(nome, sobrenome))
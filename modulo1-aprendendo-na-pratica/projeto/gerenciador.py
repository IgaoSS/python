# Projeto de lista de tarefas

# Função para adicionar tarefa
def adicionar_tarefa(nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa [{nome_tarefa}] foi adicionada com sucesso!")
    return

# Função para ver todas as tarefas
def ver_tarefas():
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

# Função para atualizar o nome da tarefa
def atualizar_tarefa(indice_tarefa, novo_nome_tarefa):
    indice_ajustado = int(indice_tarefa) - 1

    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"\nTarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("\nÍndice de tarefa inválido!")
    return

# Função para completar as tarefas
def completar_tarefa(indice_tarefa):
    indice_ajustado = int(indice_tarefa) - 1

    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["completada"] = True
        print(f"\nTarefa {indice_tarefa} completada")
    else:
        print("\nÍndice de tarefa inválido!")
    return

# Função para deletar todas tarefas completadas
def deletar_tarefas_concluidas():
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("\nTarefas concluídas foram deletadas")
    return


tarefas = []

while True:
    print("\n======== MENU DO GERENCIADOR DE LISTA DE TAREFAS ========")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Concluídas")
    print("6. Sair do programa")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(nome_tarefa)
    
    elif escolha == "2":
        ver_tarefas()
    
    elif escolha == "3":
        ver_tarefas()
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(indice_tarefa, novo_nome)
    
    elif escolha == "4":
        ver_tarefas()
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(indice_tarefa)
    
    elif escolha == "5":
        deletar_tarefas_concluidas()
        ver_tarefas()

    elif escolha == "6":
        break

print("Programa Finalizado")
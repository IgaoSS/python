#☆

contacts = []

# Função para adicionar um novo contato
def addContact():
    name = input("Informe o nome do contato: ")
    phone = input("Informe o telefone do contato: ")
    email = input("Informe o e-mail do contato: ")
    favorite = False

    newContact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite
    }

    contacts.append(newContact)
    return

# Função para exibir todos os contatos
def showAllContacts():
    print(f"\n------ Lista de contatos")

    for index, contact in enumerate(contacts):
        newIndex = index + 1
        contactName = contact["name"]
        contactPhone = contact["phone"]
        contactEmail = contact["email"]
        contactFavorite = "★" if contact["favorite"] else "☆"

        print(f"\n- Contato {newIndex}")
        print(f"    ◦ Nome: {contactName}")
        print(f"    ◦ Telefone: {contactPhone}")
        print(f"    ◦ E-mail: {contactEmail}")
        print(f"    ◦ Favorito: [ {contactFavorite} ]")
    return

# Função para atualizar os dados de um contato
def updateContact():
    index = input("\nInforme o código do contato que deseja atualizar: ")
    newIndex = int(index) - 1
        
    if(checkIndexIsValid(newIndex)):
        name = input("Informe o novo nome do contato: ")
        phone = input("Informe o novo telefone do contato: ")
        email = input("Informe o novo e-mail do contato: ")

        contacts[newIndex]["name"] = name
        contacts[newIndex]["phone"] = phone
        contacts[newIndex]["email"] = email

        print(f"\nContato {index} atualizado com sucesso !")
    else:
        print("\nCódigo de contato inválido !")
    return

# Função para atualizar se um contato é favorito ou não
def updateFavoriteStatus():
    index = input("\nInforme o código do contato que deseja alterar o status de favorito: ")
    newIndex = int(index) - 1

    if(checkIndexIsValid(newIndex)):
        newStatus = not contacts[newIndex]["favorite"]
        contacts[newIndex]["favorite"] = newStatus
        newStatusMsg = "marcado" if newStatus else "desmarcado"

        print(f"Contato {index} foi {newStatusMsg} como favorito")
    else:
        print("\nCódigo de contato inválido !")
    return

# Função para exibir a lista de todos os contatos favoritos
def showAllFavoriteContacts():
    print(f"\n------ Lista de contatos favoritos")
    
    for index, contact in enumerate(contacts):
        if contact["favorite"]:
            newIndex = index + 1
            contactName = contact["name"]
            contactPhone = contact["phone"]
            contactEmail = contact["email"]
            contactFavorite = "★" if contact["favorite"] else "☆"

            print(f"\n- Contato {newIndex}")
            print(f"    ◦ Nome: {contactName}")
            print(f"    ◦ Telefone: {contactPhone}")
            print(f"    ◦ E-mail: {contactEmail}")
            print(f"    ◦ Favorito: [ {contactFavorite} ]")
    return

# Função para delete um contato
def deleteContact():
    index = input("\nInforme o código do contato que deseja excluir: ")
    newIndex = int(index) - 1
    
    if(checkIndexIsValid(newIndex)):
        del contacts[newIndex]
        print(f"\nContato {index} excluído com sucesso !")
    else:
        print("\nCódigo de contato inválido !")
    return

def checkIndexIsValid(index):
    if index >= 0 and index < len(contacts):
        return True
    else:
        return False

while True:
    print("\n========= AGENDA DE CONTATOS =========")
    print("1. Salvar um novo contato")
    print("2. Ver lista de todos os contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Deletar contato")
    print("7. Fechar agenda")

    choose = input("\nEscolha uma opção: ")
    print() # Apenas para dar um espaço

    if choose == "1":
        addContact()
    elif choose == "2":
        showAllContacts()
    elif choose == "3":
        showAllContacts()
        updateContact()
    elif choose == "4":
        showAllContacts()
        updateFavoriteStatus()
    elif choose == "5":
        showAllFavoriteContacts()
    elif choose == "6":
        showAllContacts()
        deleteContact()
    elif choose == "7":
        break
    else:
        print("\nOpção inválida. Por favor, tente novamente.")

print("\nPrograma finalizado")
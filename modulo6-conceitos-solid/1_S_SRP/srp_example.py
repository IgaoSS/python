class Process:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str): #1
            print("Acessando o banco de dados...") #2
            print("Verificando existência do usuário...")
            print("Cadastro de usuários realizado com sucesso!") #3
        else:
            raise Exception("Dados inválidos!")
        
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
# Correções na classe seguindo os princípios do SRP
class ProcessSRP:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error("Dados inválidos!")
        
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
    def __verify_input_in_database(self, username: str) -> None:
        print("Acessando o banco de dados...")
        print("Verificando existência do usuário...")

    def __insert_new_user(self, username: str, password: str) -> None:
        print("Cadastro de usuários realizado com sucesso!")

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)
class MyClass:
    # Método público
    def register(self) -> None:
        print('Iniciando o método de registro')
        self.__verify_data()
        self.__verify_register()
        self.__insert_data()

    # Método privado
    def __verify_data(self) -> None:
        print('Verificando os dados')

    # Método privado
    def __verify_register(self) -> None:
        print('Verificando o registro')

    # Método privado
    def __insert_data(self) -> None:
        print('Inserindo os dados')

obj = MyClass()

obj.register()
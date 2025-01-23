'''
exc_type: O tipo da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_value: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu.
    Se não ocorreu nenhuma exceção, este parâmetro será None.
'''

class Something:
    '''teste'''
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with Something() as something:
    print("Lógica do with")
        
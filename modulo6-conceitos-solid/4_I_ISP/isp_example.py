# Uma classe para trabalhar com arquivos PDF, txt e Excel
from abc import ABC, abstractmethod

# É uma clase bem genérica que pode atender PDF, txt ou Excel
# Isso vai contra o princípio de segregação de interface
class Document(ABC):
    @abstractmethod
    def load(self): pass

    # Método para ver o PDF
    @abstractmethod
    def view(self): pass

    # Método para formatar o txt
    @abstractmethod
    def format(self): pass

    # Método para calcular uma coluna do excel
    @abstractmethod
    def calculate(self): pass

# Ao rodar somente assim, dará erro, porque não adicionou as outras classes, mesmo que não seja utilizado para o PDF
class PDF(Document):
    def load(self):
        print("Carregando PDF...")

    def view(self):
        print("Visualizando PDF...")

    def format(self):
        print("Sem uso")

    def calculate(self):
        print("Sem uso")

document1 = PDF()


# Correções na classe seguindo os princípios do ISP
class DocumentPDF:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentExcel:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass

class Excel(DocumentExcel):
    def load(self):
        print("Carregando Excel...")
    
    def calculate(self):
        print("Calculando Coluna Excel...")
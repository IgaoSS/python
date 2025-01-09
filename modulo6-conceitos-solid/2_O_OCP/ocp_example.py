from abc import ABC, abstractmethod

class Company:
    def do_work(self, worker: int) -> None:
        if worker == 1:
            print("Programmer creating code")
        elif worker == 2:
            print("Seller selling the product")
        elif worker == 3:
            print("Human Resources hiring new devs")
        else:
            print("Error, no Worker!")

company = Company()
company.do_work(1)

print()

# Correções na classe seguindo os princípios do OCP
# Caso queira adicionar novos trabalhadores, o IF irá aumentar até atender todos funcionários

class Employee(ABC):
    @abstractmethod
    def make(self) -> None:
        pass

class Programmer(Employee):
    def make(self) -> None:
        print("Programmer creating code")

class Seller(Employee):
    def make(self) -> None:
        print("Seller selling the product")

class HR(Employee):
    def make(self) -> None:
        print("Human Resources hiring new devs")

class CompanyOCP:
    def do_work(self, worker: any) -> None:
        worker.make()

programmer = Programmer()
seller = Seller()
hr = HR()
company_ocp = CompanyOCP()

company_ocp.do_work(programmer)
company_ocp.do_work(seller)
company_ocp.do_work(hr)
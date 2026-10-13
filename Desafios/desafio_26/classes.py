from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome = '', sal_bruto = 0, salario = 0, sal_minimo = 1612, inss = 7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_minimo = sal_minimo
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        pass


class Horista(Funcionario):

    def __init__(self, nome, valor_hora = 0, horas_trab = 0):
        super().__init__(nome)
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

       
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * 7.5 / 100)
        print(f"{self.nome}, salário bruto de: R${self.sal_bruto}, e liquido de: R${self.salario}")


class Mensalista(Funcionario):

    pass
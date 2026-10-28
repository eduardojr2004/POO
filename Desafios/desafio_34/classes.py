from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario


    def __str__(self):
        valor_do_bonus = self.calcular_bonus()
        return f"O salário de: {self.nome} é: R$ {self._salario} e tem bônus de: R$ {valor_do_bonus}"    


    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > self._salario:
            self._salario = novo_salario

        else:
            print(f"O novo salário não pode ser MENOR que o salário atual!")


#Gerente 15%
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        bonus = self._salario * 0.15
        return bonus

    
#Desenvolvedor 10%
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonus = self._salario * 0.10
        return bonus


#Designer 8%
class Designer(Funcionario):
    def __init__(self, nome, salario):
            super().__init__(nome, salario)
    
    def calcular_bonus(self):
        bonus = self._salario * 0.08
        return bonus


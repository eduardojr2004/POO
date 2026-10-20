
class Conta:

    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self.__saldo = 100


    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado! nome: {self.nome}, conta: {self.conta}, cpf/cnpj: {self.cpf_cnpj}, novo saldo: {self.saldo}")
            
        else:
            print("Valor a depositar inválido!")


class Pf(Conta):

    def __init__(self, nome, conta, cpf_cnpj):
        super().__init__(nome, conta)
        self.cpf_cnpj = cpf_cnpj
        print(f"Os dados são, nome: {self.nome}, conta: {self.conta}, cpf/cnpj: {self.cpf_cnpj} e saldo inicial: {self.saldo}")

        

class Pj(Conta):

    pass
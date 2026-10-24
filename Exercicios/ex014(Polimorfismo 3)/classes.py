from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self,valor):
        print(f"Não foi possível analisar o valor: {valor}")

    @analisar.register
    def _(self, valor: int):
        print(f"{valor} é um número INTEIRO.")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um PONTO FLUTUANTE.")

    @analisar.register
    def _(self, valor: str):
        print(f"{valor} é uma CADEIA DE CARACTERES.")

    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} é uma COLEÇÃO DE DADOS.")
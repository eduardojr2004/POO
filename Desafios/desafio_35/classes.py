from abc import ABC, abstractmethod
from functools import singledispatchmethod

class Arquivo(ABC):

    def __init__(self, nome, extensao, tamanho):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        extensoes = ["pdf", "doc"]

        if valor in extensoes:
            self._extensao = valor
        else:
            raise AttributeError("Extensão não permitida!")


    @abstractmethod
    def abrir(self):
        pass


class Pdf(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        novo_tamanho = self.tamanho / 1000000
        print(f"Abrindo o arquivo: {self.nome}.pdf de tamanho: {novo_tamanho}mb no Adobe.")

    
class Doc(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, "doc", tamanho)

    def abrir(self):
            novo_tamanho = self.tamanho / 1000000
            print(f"Abrindo o arquivo: {self.nome}.doc de tamanho: {novo_tamanho}mb no Word.")


def abrir_arquivo(arquivo):
    arquivo.abrir()
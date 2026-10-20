from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"{ano} é um ano inválido")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento.")

    @abstractmethod
    def apresentar(self):
        pass


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome, nasc, curso):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso: {curso} não esta na lista de cursos oficiais.")

    @classmethod
    def add_curso(cls, novo_curso):
        novo_curso = novo_curso.strip().upper()

        if 3 <= len(novo_curso) <= 5:
            Aluno.cursos_oficiais.append(novo_curso)
        else:
            raise ValueError(f"Nome do curso: {novo_curso} esta fora do padrão.")

    def apresentar(self):
        return f"Olá, sou {self._nome}, tenho {self.idade} anos e estudo {self.curso}."

    def __str__(self):
        return f"Aluno(Nome: {self._nome}, Nasc: {self.nascimento}, Curso: {self.curso})"
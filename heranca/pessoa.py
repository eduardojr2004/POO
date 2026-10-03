"""
    Cria a classe Pessoa que é a classe mãe que possue os atributos em comum das demais classes:
    - Aluno
    - Professor
    - Funcionário

    E o método fazer_aniversário
"""

class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
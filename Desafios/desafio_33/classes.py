import datetime

class Pessoa():

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self._idade = 0

        
class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ING"]

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = curso


    @property
    def idade(self):
        ano_atual = datetime.date.today().year
        if self.nascimento < ano_atual:
            self._idade = ano_atual - self.nascimento
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        print(f"Negado! A idade não pode ser alterada para {valor}. Ela é calculada automaticamente.")


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,valor):
        if 3 <= len(valor) <= 5 and valor in self.cursos_oficiais:
                    self._curso = valor
        else:
            print("O curso esta fora do padrão ou já existe!")


    def add_curso(self, curso):
        if 3 <= len(curso) <= 5 and curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)
        else:
            print("O curso esta fora do padrão ou já existe!")
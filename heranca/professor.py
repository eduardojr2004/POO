from POO.heranca.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade = "", nivel = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula.")
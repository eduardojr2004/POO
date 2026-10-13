from POO.heranca.pessoa import Pessoa

class Aluno(Pessoa):
        # Na chamada do aluno precisa passar: nome, idade, curso e turma
    def __init__(self, nome="", idade=0, curso="", turma=""):
        # Utiliza o super para passar parâmetros para a mãe, se não 
        # pega os dados padrão definidos na mãe
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer a matricula")
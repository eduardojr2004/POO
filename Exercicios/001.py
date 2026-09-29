# DECLARACAO DE CLASSE
class Cliente:
    def __init__(self): #MÉTODO CONSTRUTOR
        #ATRIBUTOS DE INSTÂNCIA
        self.nome = ''
        self.idade = 0

    # MÉTODOS DE INSTÂNCIA
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é cliente e tem {self.idade} anos de idade."


#DECLARACAO DE OBJETOS
c1 = Cliente()
c1.nome = 'Maria'
c1.idade = 17
c1.aniversario()
print(c1.mensagem())

c2 = Cliente()
c2.nome = 'Mauro'
c2.idade = 53
c2.aniversario()
print(c2.mensagem())

c3 = Cliente()
print(c3.mensagem())
# DECLARACAO DE CLASSE
class Cliente:
    """
    Essa classe cliente, que é uma pessoa que tem nome e idade.
    Para criar uma pessoa use, 
    variavel = Cliente(nome, idade)
    """
    def __init__(self, nome = 'vazio', idade = 0): #MÉTODO CONSTRUTOR
        #ATRIBUTOS DE INSTÂNCIA
        self.nome = nome
        self.idade = idade

    # MÉTODOS DE INSTÂNCIA
    def aniversario(self):
        self.idade += 1

    # Dumder Method
    def __str__(self):
        return f"{self.nome} é cliente e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


#DECLARACAO DE OBJETOS
c1 = Cliente('Maria', 17)
c1.aniversario()
print(c1)

c2 = Cliente('Mauro', 53)
c2.aniversario()
#print(c2)

c3 = Cliente()
#print(c3)


print(c1)         # Chama o Dumder Method para imprimir
print(c1.__dict__) # Exibicao em forma de dicionario  #Attribute
print(c1.__getstate__()) # Method # Personalizavel
print(c1.__class__)
print(c1.__doc__) # Exibe a documentacao
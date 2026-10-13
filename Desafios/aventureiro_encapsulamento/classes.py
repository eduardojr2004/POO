
class Aventureiro():

    def __init__(self, nome, categoria, life = 500):
        self.nome  = nome
        self.categoria = categoria
        self.__life = life

    def __str__(self):

        return f"Criado o herório: {self.nome}, da categoria: {self.categoria} com: {self.life} de vida."


# A cada chamada do método o personagem recebe 250 de life
    def pocao(self):

        self.life += 250


    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, valor):
        self.__life = valor
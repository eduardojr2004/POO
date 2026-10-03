class Aventureiro:

    def __init__(self, id_jogador, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.nivel = 1
        self.vida = 100
        self.jogador = id_jogador
        

    def __str__(self):
        return f"O jogador {self.jogador} tem nome: {self.nome}, sua especialidade é: {self.especialidade}, sua vida é: {self.vida} e seu level é: {self.nivel}"


    def aumentar_vida(self, qtd):
        self.vida += qtd

    def diminuir_vida(self, qtd):
        self.vida -= qtd

    def aumentar_nivel(self, qtd):
        self.nivel += qtd

    def diminuir_nivel(self, qtd):
        self.nivel -= qtd

    
j1 = Aventureiro("1", "Gandalf", "Mago")
j2 = Aventureiro("2", "Aragorn", "Tank")

j1.aumentar_nivel(10)
j1.diminuir_nivel(2)
j1.aumentar_vida(50)

j2.aumentar_vida(30)
j2.aumentar_nivel(7)

print(j1)
print(j2)
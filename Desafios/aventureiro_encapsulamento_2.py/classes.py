import random

class Aventureiro:

    def __init__(self, nome, classe, life):
        self.nome = nome
        self.classe = classe.lower()
        self._life = life

                
class Personagem(Aventureiro):


    def __init__(self, nome, classe, life, weapon):
        super().__init__(nome, classe, life)
        self.weapon = weapon


    def receber_dano(self, dano_sofrido):
            
            self._life -= dano_sofrido
    
            if self._life > 0:
    
                print(f"{self.nome} recebeu: {dano_sofrido} de dano! A vida restante é: {self._life}")
    
            else:
                self._life = 0
                print(f"{self.nome} recebeu: {dano_sofrido} de dano e caiu! Vida: {self._life}.")


    def atacar(self,alvo):

         dano = random.randint(0, 550)
         print(f"{self.nome} ataca {alvo.nome} com {self.weapon}!")

         alvo.receber_dano(dano)

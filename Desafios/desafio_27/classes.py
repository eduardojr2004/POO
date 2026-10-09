from abc import ABC,abstractmethod
import random

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"O jogador: {self.nome} de vida: {self.vida}, atacou {alvo.nome} com um golpe {golpe} de força: {forca}")
            alvo.receber_dano(forca)

        else:
            print(f"O golpe de: {self.nome} não pode ser aplicado em: {alvo.nome}")


    def receber_dano(self, dano):
        fator = random.randrange(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu um dano de: {fator}")

    @abstractmethod
    def curar(self):
        pass



class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de machado", "Pulo Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator

        print(f"{self.nome} enrolou atadura nos ferimentos e recuperou {fator} de vida")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de Luz", "Magia estática"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"{self.nome} fez uma magia de cura e recuperou: {fator} de vida.")
import random
from abc import ABC, abstractmethod
from functools import singledispatchmethod


class PocaoVida:
    pass


class AmuletoForca:
    pass


class Personagem(ABC):

    def __init__(self, nome, vida = 100, ataque = 10):
        self.nome = nome
        self._vida = vida
        self._ataque = ataque


    @abstractmethod
    def atacar(self, alvo):
        pass


    def receber_dano(self, quantidade_dano):

        self._vida -= quantidade_dano
        print(f"POW! {self.nome} recebeu: {quantidade_dano} de dano!")


    def __str__(self):

        return f"{self.nome} tem {self._vida} de vida.\n"


class Guerreiro(Personagem):

    def __init__(self, nome, vida = 100, ataque = 15, armadura = 5):
        super().__init__(nome, vida, ataque)
        self._armadura = armadura


    def atacar(self, alvo):
        print(f"O guerreiro ataca com a espada!")
        alvo.receber_dano(random.randint(0, 40))
        

    def receber_dano(self, quantidade_dano):
        
        dano_real = quantidade_dano - self._armadura

        if dano_real < 0:
            dano_real = 0

        self._vida -= dano_real

        print(f"CLANG! Golpe de {quantidade_dano}. A armadura de {self.nome} bloqueou {self._armadura}!")
        print(f"Dano real sofrido: {dano_real}")


    @singledispatchmethod 
    def usar_item(self,item):
        print("O guerreiro olha confuso para o item")

    @usar_item.register(PocaoVida)
    def _(self, item):
        self._vida += 30

    @usar_item.register(AmuletoForca)
    def _(self, item):
        self._ataque += 10


class Mago(Personagem):

    def __init__(self, nome, mana, vida= 100, ataque= 10):
        super().__init__(nome, vida, ataque)
        self._mana = mana


    def atacar(self, alvo):
        print(f"{self.nome} ataca com a bola de fogo!")
        alvo.receber_dano(random.randint(0, 20))


    def __str__(self):
        return f"{self.nome} tem: {self._vida} de vida e {self._mana} de mana"


    def receber_dano(self, quantidade_dano):
                
            self._vida -= quantidade_dano
    
            print(f"{self.nome} recebeu: {quantidade_dano} de dano! Sua vida agora é: {self._vida}")
            

class Dragao(Personagem):

    def __init__(self, nome, vida=500, ataque=50, casco = 10):
        super().__init__(nome, vida, ataque)
        self.casco = casco


    def atacar(self, alvo):
        print(f"O {self.nome} ataca {alvo.nome} com bola de fogo!!")
        alvo.receber_dano(random.randint(0,50))


    def receber_dano(self, quantidade_dano):
            
            dano_real = quantidade_dano - self.casco
    
            if dano_real < 0:
                dano_real = 0
    
            self._vida -= dano_real
    
            print(f"CLANG! Golpe de {quantidade_dano}. O casco de {self.nome} bloqueou {self.casco}!")
            print(f"Dano real sofrido: {dano_real}")
    def __str__(self):
    
        return f"{self.nome} tem {self._vida} de vida.\n"
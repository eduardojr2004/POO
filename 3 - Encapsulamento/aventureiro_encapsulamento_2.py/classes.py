import random

class Aventureiro:

    def __init__(self, nome, life):
        self.nome = nome
        self._life = life


    def receber_dano(self, dano, bloqueio):

        dano_sofrido = max(0, dano - bloqueio)
        # Se o bloqueio for MAIOR ou IGUAL ao dano, o dano_sofrido será 0!
    
        if dano_sofrido == 0:
            print(f"🛡️ INCRÍVEL! {self.nome} bloqueou totalmente o ataque!\n")
            return 

        # Se o código chegou até aqui, é porque tomou algum dano!
        self._life -= dano_sofrido

        if self._life > 0:
            print(f"💥 {self.nome} recebeu {dano_sofrido} de dano! A vida restante é: {self._life}\n")
        else:
            self._life = 0
            print(f"💀 {self.nome} recebeu {dano_sofrido} de dano e caiu! Vida: {self._life}.\n")

    def descansar(self):

          self._life += 500
          print(f"{self.nome} descansou e recebeu 500 de vida! Sua vida agora é: {self._life}\n")
    
                
class Mago(Aventureiro):

    def __init__(self, nome, life):
        super().__init__(nome, life)
        

    def atacar(self,alvo):
    
             dano = random.randint(0, 1500)
             print(f"{self.nome} ataca {alvo.nome} com o cajado!\n")
    
             alvo.bloquear_ataque(dano)


    def bloquear_ataque(self, dano):

         bloqueio = random.randint(0, 150)
         print(f"{self.nome} conseguiu bloquear {bloqueio} de dano!\n")
         self.receber_dano(dano, bloqueio)


class Escudeiro(Aventureiro):


    def __init__(self, nome, life):
        super().__init__(nome, life)

        
    def atacar(self,alvo):

                dano = random.randint(0, 1000)
                print(f"{self.nome} ataca {alvo.nome} com a espada!\n")

                alvo.bloquear_ataque(dano)

    def bloquear_ataque(self, dano):
    
             bloqueio = random.randint(0, 180)
             print(f"{self.nome} conseguiu bloquear {bloqueio} de dano!\n")
             self.receber_dano(dano, bloqueio)


class Arqueiro(Aventureiro):


    def __init__(self, nome, life):
        super().__init__(nome, life)

        
    def atacar(self,alvo):

                dano = random.randint(0, 750)
                print(f"{self.nome} ataca {alvo.nome} com o arco!\n")

                alvo.bloquear_ataque(dano)


    def bloquear_ataque(self, dano):

            bloqueio = random.randint(0, 120)
            print(f"{self.nome} conseguiu bloquear {bloqueio} de dano!\n")
            self.receber_dano(dano, bloqueio)


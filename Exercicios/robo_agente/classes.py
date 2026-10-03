# Importamos as ferramentas para criar "Contratos" (Classes Abstratas)
from abc import ABC, abstractmethod

# 1. NOSSO CHASSI BÁSICO
class Robo():

    # O método __init__ é o "nascimento" do robô.
    def __init__(self, nome = "", bateria = 100):
        self.nome = nome
        self.bateria = bateria

    # O método __str__ diz como o robô se apresenta se tentarmos "imprimi-lo" na tela.
    def __str__(self):
        
        return f"O {self.nome} esta com {self.bateria}% de carga."


# 2. O ROBÔ COM UPGRADE DE ASAS (Herda tudo do Robo)
class RoboVoador(Robo):

    def voar(self):

        # Verifica se tem energia antes de gastar
        if self.bateria < 10:
            print(f"Bateria insuficiente para o {self.nome} voar! Carga: {self.bateria}%")

        else:
            self.bateria -= 10
            print(f"Sou o robô {self.nome} estou voando! Bateria restante: {self.bateria}%")


# 3. O CONTRATO (Classe Abstrata)
class RoboModelo(Robo, ABC):

    @abstractmethod     # Isso é a assinatura do contrato!
    def trabalhar(self):
        # O 'pass' significa: "Não vou dizer COMO trabalha aqui, 
        # quem herdar de mim que se vire para explicar!"
        pass


# 4. O FUNCIONÁRIO (Herda o contrato)
class RoboLimpeza(RoboModelo):

    # Ele é OBRIGADO a criar essa função, senão o Python daria erro.
    def trabalhar(self):
        if self.bateria >= 5:
            print(f"O {self.nome} está limpando agora! Sua carga é: {self.bateria}%")

        else:
            print(f"O {self.nome} não pode limpar agora a bateria esta em: {self.bateria}%")
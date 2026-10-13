# Importamos as ferramentas para criar "Contratos" (Classes Abstratas)
from classes import Robo, RoboVoador, RoboLimpeza, RoboModelo            


def main():

    r1 = Robo("Robo 01")
    print(r1)

    r2 = RoboVoador("Robo 02", bateria = 25)
    print(r2)

    r3 = RoboVoador("Robo 03", bateria = 25)
    print(r3)

    r4 = RoboLimpeza("Robo 04", bateria = 25)

    r2.voar()
    r2.voar()
    r2.voar()
    
    r3.voar()

    r4.trabalhar()

if __name__ == "__main__":
    main()
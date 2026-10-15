from classes import Aventureiro, Personagem
from rich import inspect

def main():

    p1 = Personagem("Gandalf", "Mage", 1500, "Cajado")
    p2 = Personagem("Aragorn", "Tank", 2500, "Espada")
    p3 = Personagem("Legolas", "Archer", 1200, "Arco")
    p1.atacar(p2)
    p2.atacar(p1)
    print("\n--Inspecionando o herói--")
    inspect(p1, methods=True, private=True)
    inspect(p2, methods=True, private=True)
    inspect(p3, methods=True, private=True)



if __name__ == "__main__":
    main()
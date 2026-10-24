from classes import Aventureiro, Mago, Escudeiro, Arqueiro
from rich import inspect

def main():

    p1 = Mago("Gandalf", 1000)
    p2 = Escudeiro("Aragorn", 1500)
    p3 = Arqueiro("Legolas", 1200)

    while p1._life > 0 and p2._life > 0:

        input("")          
        p1.atacar(p2)

        if p2._life > 0:
            p2.atacar(p1)
        print("-" * 40)

    print("🏆 A BATALHA TERMINOU!")
    if p1._life > 0:
        print(f"{p1.nome} é o vencedor!")
        p1.descansar()

    else:
        print(f"{p2.nome} é o vencedor!")
        p2.descansar()
        
    #print("\n--Inspecionando o herói--")
    #inspect(p1, methods=True, private=True)
    #inspect(p2, methods=True, private=True)
    #inspect(p3, methods=True, private=True)

if __name__ == "__main__":
    main()
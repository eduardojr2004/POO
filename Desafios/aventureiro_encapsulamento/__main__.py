from classes import Aventureiro


def main():

    j1 = Aventureiro("Gandalf", "Mago", 1000)
    print(j1)
    j1.pocao()

    print(f"A vida atual do {j1.nome} é: {j1.life}")

    j1.life = 600
    print(f"A vida atual do {j1.nome} é: {j1.life}")



if __name__ == "__main__":
    main()
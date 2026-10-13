from classes import Personagem, Guerreiro, Mago

def main():

    j1 = Mago("Merlin", 3000)
    j2 = Guerreiro("Cratos", 2500)

    j1.atacar(j2, 200)
    j2.atacar(j1, 200)



if __name__ == "__main__":
    main()
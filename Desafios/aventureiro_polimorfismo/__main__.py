from classes import Personagem, Guerreiro, Mago, Dragao, PocaoVida, AmuletoForca


def main():

    h1 = Guerreiro("Arthur")
    m1 = Mago("Gandalf", 30)
    chefao = Dragao("Smaug")

    print("--- 🎒 Preparação para a Batalha ---")
    pocao = PocaoVida()
    amuleto = AmuletoForca()

    h1.usar_item(pocao)
    h1.usar_item(amuleto)
    h1.usar_item("Corda velha")

    print("\n--- ⚔️ A Batalha Final ⚔️ ---")

    """ print("--- Inicio da aventura ---")
    print(h1)
    print("Uma armadilha!")
    h1.receber_dano()
    print("Depois da armadilha:")
    print(h1)

    print("--- A vez do mago ---")
    print(m1)
    print("O mago pisou em espinhos")
    m1.receber_dano()
    print("Depois dos espinhos")
    print(m1) """

    """ h1.atacar(m1)
    m1.atacar(h1) """
    #chefao.atacar(m1)
    #h1.atacar(chefao)
    grupo_herois = [h1,m1]
    for heroi in grupo_herois:
        heroi.atacar(chefao)

    print(chefao)



if __name__ == "__main__":

    main()
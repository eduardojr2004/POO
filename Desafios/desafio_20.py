class Gamer:
    """
    Cria uma classe com o nome do gamer e seus jogos favoritos
    """

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favoritos(self, game):
        self.favoritos.append(game)
        #self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: {self.nome}\n"
        conteudo += f"Nick: {self.nick}\n"
        conteudo += f"Jogos favoritos:\n"

        for game in self.favoritos:
            conteudo += f"{game}\n"

        return conteudo

j1 = Gamer("Fabricio da Silva", "detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
print(j1.ficha())
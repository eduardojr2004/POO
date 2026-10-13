from rich import inspect

class Gamer:

    """
    Cria uma classe Gamer, que contem o nome real, nick e jogos favoritos. E cria um metodo para mostrar os jogos favoritos
    """

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def __str__(self):
        conteudo = f"O nome real do jogador é: {self.nome}\n"
        conteudo += f"O nick do jogador é: {self.nick}\n"
        conteudo += f"Os jogos favoritos são:\n"
        
        for favorito in self.favoritos:
           conteudo += f"{favorito}\n"

        return(conteudo)

        


j1 = Gamer("Fabricio da Silva", "detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("Fifa")
#inspect(j1)
print(j1)
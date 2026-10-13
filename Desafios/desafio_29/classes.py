
class Diario():

    def __init__(self):
        self._listas = []


    def ler(self, senha):
        if senha == 123456:
            print("Senha correta, lendo o diário:")
            for lista in self._listas:
                print(f"{lista}")
        else:
            print("Senha errada!")


    @property
    def lista(self):
        return self._listas

    @lista.setter
    def lista(self, valor):
        self._listas.append(valor)
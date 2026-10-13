from rich import print

class Caneta:
    
    def __init__(self, cor):
        match cor.lower().strip():

            case ("azul"):
                self.cor = "blue"

            case ("verde"):
                self.cor = "green"

            case ("vermelho" | "vermelha"):
                self.cor = "red"

            case _:
                raise ValueError("Cor inválida!")

        self.tampada = True
    
    
    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A [{self.cor}]caneta[/] esta tampada!")

        else:
            print(f"Esta sendo escrito na cor: [{self.cor}]{msg}[/]")

        

c1 = Caneta("azul")
c2 = Caneta("verde")
c3 = Caneta("vermelha")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c2.escrever("Hello World!")
c3.escrever("Phyton!")
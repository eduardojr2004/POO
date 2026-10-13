from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        
        print(f"Fervendo a água a 100 graus Celsius.")
        self.misturar()
        self.servir()


    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        print(f"Passando água pressurizada pelo pó do café moído.")

    def servir(self):
        print(f"Servindo em uma xícara pequena.")

class Cha(BebidaQuente):

    def misturar(self):
        print(f"Mergulhando o sachê de ervas na água.")
    
    def servir(self):
        print("Servindo na caneca de porcelana com limão.")

class Leite(BebidaQuente):
    def misturar(self):
        print(f"Passando vapor pressurizado pelo bico do leite.")
    
    def servir(self):
        print(f"Servindo na caneca grande, já com café.")
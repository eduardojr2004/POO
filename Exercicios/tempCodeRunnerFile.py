from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, comprimento):
        self.comprimento = comprimento

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, comprimento):
        self.comprimento = comprimento
    

    def perimetro(self):
        
        print(f"O perímetro do Quadrado é: {4 * self.comprimento}")

    def area(self):

        print(f"A área do Quadrado é: {self.comprimento * self.comprimento}")


class Circulo(Poligono):

    def __init__(self, comprimento):
        super().__init__(comprimento)
        self.raio = comprimento

    def perimetro(self):
        print(f"O perímetro do circulo é: {2 * 3.14 * self.raio}")

    def area(self):
        print(f"A área desse círculo é: {3.14 * (self.raio + self.raio)}")
    



def main():

    q1 = Quadrado(6)
    q1.perimetro()
    q1.area()

    c1 = Circulo(9)
    c1.perimetro()
    c1.area()
    

if __name__ == "__main__":
    main()
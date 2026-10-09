from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia = 0):

        self.distancia = distancia
       

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
                

    def calc_frete(self):
        print(f"O frete para a Moto é: {self.distancia * 0.5}")
        

class Caminhao(Transporte):

    def __init_subclass__(cls):
        return super().__init_subclass__()
        

    def calc_frete(self):
        
        if self.distancia < 50:
            print(f"A distância de: {self.distancia} é menor que a permitido.")

        else:
            print(f"O frete para a distância de: {self.distancia} de Caminhão é: R$ {self.distancia * 1.20:.2f}")
    

class Drone(Transporte):

    def __init_subclass__(cls):
        return super().__init_subclass__()

    def calc_frete(self):
        if self.distancia > 10:
            print(f"A distância de: {self.distancia} é maior que a permitido.")
        
        else:
            print(f"O frete para a distância de: {self.distancia} de Drone é: R$ {self.distancia * 9.50:.2f}")
class Termostato:

    @property
    def temperatura(self):
        return self.__temperatura
        
    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16:
            self.__temperatura = 16

        elif valor > 30:
            self.__temperatura = 30

        elif valor % 5 != 0:
            raise ValueError(f"Valor:{valor}{chr(176)}C inválido!")

        else:
            self.__temperatura = valor


    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"
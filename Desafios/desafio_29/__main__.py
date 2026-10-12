from rich import inspect
from classes import Diario

def main():

    d1 = Diario()

    d1.lista = "Primeira frase"
    d1.lista = "Segunda frase"
    #inspect(d1, private=True, methods=True)

    d1.ler(123456)

if __name__ == "__main__":
    
    main()
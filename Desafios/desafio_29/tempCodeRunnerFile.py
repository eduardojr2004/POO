from rich import inspect
from classes import Diario

def main():

    d1 = Diario()

    d1.escrever("Primeira frase")
    d1.escrever("Segunda frase")
    inspect(d1, private=True, methods=True)

if __name__ == "__main__":
    
    main()
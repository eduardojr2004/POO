from classes import Retangulo
from rich import inspect

def main():

    r1 = Retangulo()
    try:
        r1.base = 12
        r1.altura = 7
        r1.medidas = (8, 12)

    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
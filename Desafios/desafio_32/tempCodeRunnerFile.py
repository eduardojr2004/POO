from classes import ContaBancaria

def main():

    c1 = ContaBancaria(1234, "Pedro", 3000, "123456")

    c1.sacar(500)
    print(c1) 

    c1.nome = "Maricota"
    print(c1)
    
if __name__ == "__main__":
    main()
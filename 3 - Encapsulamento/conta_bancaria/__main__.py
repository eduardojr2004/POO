from classes import Conta, Pf, Pj

def main():

    c1 = Pf("Pedro", 123456, "01966262507")
    c1.saldo = 1000

    print(c1.__dict__)

if __name__ == "__main__":
    main()
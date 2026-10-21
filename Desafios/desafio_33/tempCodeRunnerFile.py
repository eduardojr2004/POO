from classes import Pessoa, Aluno

def main():
    a1 = Aluno("Pedro", 2000, "ADM")
    print(a1.__dict__)
    print(a1.idade)
    #a1.idade = 22
    #a1.curso = "ADM"
    a1.add_curso("MODA")
    a1.curso = "ADS"
    print(Aluno.cursos_oficiais)
    print(a1.__dict__)
    



if __name__ == "__main__":
    main()
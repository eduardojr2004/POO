from classes import Pessoa, Aluno

def main():

    p1 = Aluno("Pedro", 1985, "ADM")
    p1.nascimento = 1980
    Aluno.add_curso("MODA")
    print(p1)
    print(p1.apresentar())
    print("Cursos oficiais: ", Aluno.cursos_oficiais)

    
if __name__ == "__main__":
    main()
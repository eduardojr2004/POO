class Funcionario:
    """
    Cria uma classe funcionario com os dados basicos dos funcionarios
    """

    def __init__(self, nome = 'vazio', setor = 'vazio', cargo = 'vazio'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return(f"Olá meu nome é: {self.nome}, trabalho no setor de {self.setor} no cargo de {self.cargo}.")

f1 = Funcionario("Eduardo", "TI", "Desenvolvedor")
f2 = Funcionario("Pedro", "RH", "Analista de contratações")

print(f1)
print(f2)
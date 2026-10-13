class Churrasco:

    """
    Cria uma listagem de participante:
    - Quanto de carne sera necessario(levando em consideração 400g por pessoa);
    - O custo(R$ 82.40/kg) total de carne necessário;
    - E preço por pessoa.
    """

    def __init__(self, qtd_pessoas = 0):
        self.qtd_pessoas = qtd_pessoas

        self.custos()
    
    def custos(self):
        self.qtd_carne = 0.400 * self.qtd_pessoas
        self.custo = self.qtd_carne * 82.40
        self.individual = self.custo / self.qtd_pessoas

    def __str__(self):
        return (
            f"Analisando {type(self).__name__} com {self.qtd_pessoas} pessoas:\n"
            f"Cada participante comerá 0.4kg e cada Kg custa R$ 82.40\n"
            f"Recomendado comprar {self.qtd_carne}Kg de carne\n"
            f"O custo total será de R$ {self.custo:.2f}\n"
            f"Cada pessoa pagará R$ {self.individual} para participar."
        )
        
c1 = Churrasco(15)
print(c1)
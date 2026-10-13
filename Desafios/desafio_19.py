class Livro:

    def __init__(self):
        self.atual = 0
        
    def passa_pagina(self, paginas):
        if paginas <= 0 or self.atual + paginas > 50:
            raise ValueError("Quantidade de páginas inválida!")

        else:
            self.atual += paginas
            
    def __str__(self):
        return f"A página atual é: {self.atual}"


p1 = Livro()
p1.passa_pagina(5)
p1.passa_pagina(57)
p1.passa_pagina(30)
print(p1)
class Avaliacao:
    
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo Protected (#)


    # Criando atributo Validável
    @property
    # 1. LINHA 1: É como pendurar uma placa de "Vitrine". Avisa ao Python que o método abaixo vai funcionar como uma propriedade de leitura (um "getter"). Você poderá acessar usando apenas 'objeto.nota', sem precisar de parênteses ().

    def nota(self): #getter
    # 2. LINHA 2: Definimos o nome da nossa "vitrine". O nome é 'nota'.
        
        return self._nota
        # 3. LINHA 3: Quando alguém olhar pela vitrine, retornamos o valor que está escondido no cofre (a variável '_nota'). 
        # Dica de ouro: Esse underline '_' antes do nome é uma convenção em Python que grita: "Ei programador, essa variável é secreta/privada, não mexa nela diretamente!".


    @nota.setter
    # 4. LINHA 4: Avisamos ao Python: "Lembra daquela propriedade 'nota'? Agora vou criar o Segurança (o 'setter') para ela!". Isso intercepta qualquer tentativa de usar o sinal de igual (=), como 'objeto.nota = 8'.
    def nota(self, valor):
    # 5. LINHA 5: Criamos a função do Segurança. Ela recebe o próprio objeto (self) e o novo 'valor' que alguém está tentando guardar.
        if 0 <= valor <= 10:
        # 6. LINHA 6: O Segurança faz a checagem! O novo valor é maior ou igual a 0 E menor ou igual a 10?

            self._nota = valor
            # 7. LINHA 7: Se a checagem der verdadeiro (True), o Segurança abre o cofre e guarda o valor com segurança na variável escondida '_nota'.

        else:
        # 8. LINHA 8: Se o valor for fora do permitido (ex: 15 ou -2)...
            print("Nota inválida!")
            # 9. LINHA 9: O Segurança recusa a alteração e avisa que houve um erro. O valor no cofre continua intacto!
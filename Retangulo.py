class Retangulo:

    def __init__(self):
        self.comprimento = float(input('Informe o comprimento do local '))
        self.largura = float(input('Informe a largura do local '))
    
    def setComprimento(self):
        self.comprimento = float(input('Digite o novo comprimento '))
    
    def setLargura(self):
        self.largura = float(input('Digite a nova largura '))

    def calculaAreaPerimetro(self):
        self.area = self.largura * self.comprimento
        self.perimetro = (self.largura * 2) + (self.comprimento * 2)
    
    def imprime(self):
        print(f'Serão necessários {self.area} pisos de 1x1 e {self.perimetro} rodapés.')


quarto1 = Retangulo()
quarto1.calculaAreaPerimetro()
quarto1.imprime()

quarto1.setComprimento()
quarto1.setLargura()
quarto1.calculaAreaPerimetro()
quarto1.imprime()

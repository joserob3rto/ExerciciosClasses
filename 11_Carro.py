class Carro:

    def __init__(self, consumo) -> None:
        self.consumo = consumo
        self.tanque = 0
        print(f'# {consumo} quilômetros por litro de combustível')

    def adicionarGasolina(self, litros):
        self.tanque += litros
        print(f'Abastecido com {litros} litros de combustível')
    
    def andar(self, distancia):
        self.distancia = distancia
        print(f'Andou {distancia} quilometros')

    def obterGasolina(self):
        combustivelRestante = self.tanque - (self.distancia / self.consumo)
        print(f'Restam {combustivelRestante:.2f} litros de combustível no tanque')


#Testes
meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()

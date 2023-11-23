class Tv:

    def __init__(self):
        self.volume = 0
        self.canal = 1

    def setCanal(self):
        tempCanal = int(input('Digite o número do canal: '))

        if (tempCanal > 30) or (tempCanal < 1):     
            while True:
                tempCanal = int(input('Canal não encontrado, digite um canal válido (1-30) ' ))
                if (tempCanal > 30) or (tempCanal < 1):
                    continue
                else:
                    break
            
            self.canal = tempCanal
    
    def aumentaVolume(self):
        if self.volume == 100:
            self.volume = 100
        else:
            self.volume += 1

    def diminuiVolume(self):
        if self.volume == 0:
            self.volume = 0
        else:
            self.volume -= 1
    
    def status(self):
        print(f'O volume está em {self.volume} e o canal está em {self.canal}')


#Testes:
tvquarto = Tv()
tvquarto.setCanal()
tvquarto.diminuiVolume()
tvquarto.diminuiVolume()
tvquarto.diminuiVolume()
tvquarto.diminuiVolume()
tvquarto.status()

tvsala = Tv()
tvsala.setCanal()
for _ in range(150):
    tvsala.aumentaVolume()
tvsala.status()

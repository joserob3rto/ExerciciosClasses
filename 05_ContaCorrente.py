class ContaCorrente:

    def __init__(self):
        self.conta = input('Digite o número da conta com o dígito, assim como no exemplo: xxxxx-x ')
        self.nomeCorrentista = input('Digite o nome completo do correntista ')
        self.saldo = float(0)

    def alterarNome(self):
        self.nomeCorrentista = input('Digite o novo ')

    def saque(self):
        self.saldo -= float(input('Digite o valor a ser sacado '))

    def deposito(self):
        self.saldo += float(input('Digite o valor a ser depositado '))

    def extrato(self):
        print(f'Prezado {self.nomeCorrentista}, o saldo em sua conta corrente é de {self.saldo:.2f}')


#Testes: 
contajose = ContaCorrente()
contajose.extrato()
contajose.deposito()
contajose.saque()
contajose.extrato()

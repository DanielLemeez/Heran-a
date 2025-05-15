class ContaBancaria:
    #Construtor
    def __init__(self,cpf,saldo):
        self.cpf = cpf 
        self.saldo = saldo
    
    #Funções da conta Bancaria
    def getCpf(self):
        return self.cpf
    
    def getSaldo(self):
        return self.saldo
    
    def saque(self, valorRetirar, valorAtual):
        self.saque = valorRetirar
        self.valorAtual=self.saldo-self.saque


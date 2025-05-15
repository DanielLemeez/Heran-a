class ContaBancaria:
    #Construtor
    def __init__(self,cpf,saldo):
        self.cpf = cpf 
        self.saldo = saldo
    
    #Funções da conta Bancaria

    #pegar o CPF
    def getCpf(self):
        return self.cpf
    
    #Pegar o saldo
    def getSaldo(self):
        return self.saldo
    
    #Sacar + Descontar valor da conta
    def saque(self, valorRetirar):
        self.saldo = self.saldo-valorRetirar
        


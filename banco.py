class ContaBancaria:
    #Construtor
    def __init__(self,cpf,saldo):
        self.cpf = cpf 
        self.saldo = saldo
    
    #Funções da conta Bancaria---------------

    #pegar o CPF
    def getCpf(self):
        return self.cpf
    
    def setcCpf(self,cpf):
        self.cpf=cpf
    
    #Pegar o saldo
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self):
        self.saldo = saldo
    
    #Sacar + Descontar valor da conta
    def saque(self, valorRetirar):
        #verificando se valor do saque é maior que o saldo
        #se for maior ele nega o saque, do contrario ocorre tudo normalmente.
        if(valorRetirar<=self.saldo):
            self.saldo = self.saldo-valorRetirar
            return True
        else:
            return False

    def deposito(self,deposito):
        self.saldo += deposito

        


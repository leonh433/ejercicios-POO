class CuentaBancaria:
    def __init__ (self,titular,saldo):
        self.titular = titular 
        self.__saldo = saldo #atributo privado 

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo 
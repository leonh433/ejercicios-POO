class CuentaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
   

    def set_saldo(self,nuevo_saldo):
     if nuevo_saldo >= 0:
       self.__saldo = nuevo_saldo
     else:
       print("error:el saldo no puede ser negativo ")


cuenta1 = CuentaBancaria("juan",30000)
print(cuenta1.get_saldo())

cuenta1.set_saldo(-90000)
print("saldo actualizado: ", cuenta1.get_saldo())
 


# ejercicio practico 

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad = edad 
        
nombre = input("ingrese el  nombre: ")
edad = int(input("ingrese la edad: "))       
        
e1 = Persona(nombre,edad)
print("nombre: ",e1.nombre,"y" ,"edad:",e1.edad)






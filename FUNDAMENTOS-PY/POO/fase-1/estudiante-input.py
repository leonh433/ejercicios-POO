class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota 
        
    def mostrar_info(self):
        if self.nota >= 3 :
            estado = "aprueba"
        else:
            estado = "reprueba"
        return f"nombre {self.nombre} nota:{self.nota}, estado:{estado}"
        
nombre = input("ingrese el  nombre: ")
nota = float(input("ingrese la nota: "))

e1 = Estudiante(nombre,nota)
print(e1.mostrar_info())  
class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota = nota 
        
e1 = Estudiante("juan",4.2)

print("nombre: ",e1.nombre)

e2 = Estudiante("ana", 3.8)
print("nombre: ",e2.nombre)

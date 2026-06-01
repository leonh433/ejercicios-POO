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

estudent = []

for i in range (3):
    print(f"\nregistro del estudiante {i+1}")
    nombre = input ("nombre: ")
    nota = float (input("nota"))
    
    e = Estudiante(nombre,nota)
    estudent.append(e)
    
print("\nlista de estudiante ")
for est in estudent:
    print(est.mostrar_info())
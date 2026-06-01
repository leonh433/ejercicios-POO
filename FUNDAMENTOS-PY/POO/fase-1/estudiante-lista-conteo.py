class Estudiante:
    contadoraprobados = 0
    contadornoaprobados =0
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota 
        
        if self.nota >= 3:
            Estudiante.contadoraprobados +=1
        else:
            Estudiante.contadornoaprobados +=1  
            
    def mostrar_info(self):
        if self.nota >= 3 : 
            estado = "aprueba"
            
        else:
            estado = "reprueba"
            
        return f"nombre {self.nombre} nota:{self.nota}, estado:{estado}"
    
estudent = []

for i in range(3):
    print(f"\nregistro del estudiante {i+1}")
    nombre = input ("nombre: ")
    
    while True:
        nota = float(input("ingrese la nota (0-5): "))
        if nota >=0 and nota <=5:
            break
        else:
            print("nota no valida ")                  
    
    e = Estudiante(nombre,nota)
    estudent.append(e)
    
print("\nlista de estudiante")
for est in estudent:
    print(est.mostrar_info())
    
print("\n---resumen---")
print("aprobados: ",Estudiante.contadoraprobados)
print("reprobados: ",Estudiante.contadornoaprobados)
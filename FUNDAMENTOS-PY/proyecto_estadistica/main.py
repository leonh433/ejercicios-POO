from src.estadistica import calcular_promedio
from src.estadistica import promedio_diccionario
from src.estadistica import contar_aprobados
from src.estadistica import clasificar_notas



datos = [10,15,20,25,30] 

resultado = calcular_promedio(datos)

print ("el promedio de la lista es: ",resultado)

notas = {
    "juan": 3.3,
    "ana": 4.2,
    "pedro": 4.6,
    "laura": 3.9
}
         
    

promedio_notas = promedio_diccionario(notas)
print("el promedio de las notas es: ",promedio_notas) 

aprobados = contar_aprobados(notas,4)
print("el numero de estudiantes aprobados es : ",aprobados) 

clasificacion_notas = clasificar_notas(notas)
print("clasificacion de notas: ",clasificacion_notas)
    
 
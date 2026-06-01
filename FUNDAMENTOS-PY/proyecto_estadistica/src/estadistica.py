def validar_lista(lista):
    if not lista:
        raise ValueError("la lista no puede estar vacia ")
    
    

def calcular_promedio(lista):
    validar_lista(lista)
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma/cantidad 
    return promedio 

def promedio_diccionario(diccionario):
    valores = diccionario.values()
    suma = sum(valores)
    cantidad = len(valores)
    promedio = suma/cantidad 
    return promedio 
    
    
def contar_aprobados(diccionario,nota_minima):
    valores = diccionario.values()
    contador = 0
    print(nota_minima)

    for nota in valores:
        print("entre", nota)
        if nota < nota_minima:
            contador += 1
            print(contador)
            
    
    return contador
    
def clasificar_notas(diccionario):
    valores = diccionario.values()
    resultado={
        "bajas":0,
        "medias":0,
        "altas":0
    }
    
    for nota in valores :
        if nota < 3:
            resultado["bajas"]+=1
        elif nota < 4:
            resultado["medias"]+=1
        else:
            resultado["altas"]+=1
        return resultado     
     
class Estudiante:
    def __init__(self,codigo,nombre,nota):
        self.codigo = codigo
        self.nombre = nombre 
        self.nota = nota 
        
    def estado(self):
        if self.nota >= 3:
            return "aprueba"
        else:
            return "reprueba"
        
    def mostrar_info(self):
        return f"codigo: {self.codigo} nombre: {self.nombre} nota: {self.nota} estado: {self.estado()}"
    
    
class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes =[]
        
    def registrar_estudiante(self):
        codigo = input("codigo del estudiante: ")
        
        for est in self.estudiantes:
            if est.codigo == codigo:
                print("error : el codigo ya existe")
                return
        nombre = input ("nombre: ")
        
        while True:
            nota = float(input("nota(0-5): "))
            
            if 0 <= nota <= 5:
                break
            else:
                print("nota invalida ")
                
        nuevo_estudiante = Estudiante(codigo,nombre,nota)
        self.estudiantes.append(nuevo_estudiante)
        print("estudiante registrado correctamente ")
    
    
    def mostrar_estudiantes(self):
        
        
        if len(self.estudiantes)== 0:
           print("no hay estudiantes registrado")
           
        else:
            print("\n LISTA DE ESTUDIANTES ")
            
            for est in self.estudiantes:
                print(est.mostrar_info())
                
    def buscar_estudiante(self):
        codigo_buscar = input("ingrese el codigo a buscar: ")
        
        
        for est in self.estudiantes:
            
            if est.codigo == codigo_buscar:
                print("\nEstudiante encontrado")
                print(est.mostrar_info())
                return 
        
        print("estudiante no encontrado")
        
    def eliminar_estudiante(self):
        codigo_eliminar = input("ingrese el codigo del estudiante a eliminar : ") 
        
        for est in self.estudiantes:
            if est.codigo == codigo_eliminar:
                self.estudiantes.remove(est)
                print("estudiante eliminado correctamente")
                return
            
        print("estudiante no encontrado")
        
        
    def actualizar_nota(self):
        codigo_buscar = input("ingrese el codigo del estudiante: ")
        
        for est in self.estudiantes:
            if est.codigo == codigo_buscar:
                
                while True:
                    nueva_nota = float(input("ingrese nueva nota: "))
                    
                    if 0 <= nueva_nota <= 5:
                        est.nota = nueva_nota
                        print("nota actualizada correctamente")
                        return
                    else:
                        print("nota invalida")
                        
        print("estudiante no encontrado")   
        
    def calcular_promedio(self):
        if len(self.estudiantes)== 0:
            print("no hay estudiantes registrados")
            return
        
        suma=0
        for est in self.estudiantes:
            suma+= est.nota
            promedio = suma / len(self.estudiantes)
            
            print(f"\npromedio general: {promedio: .2f}")   
            
    def guardar_archivo(self):
        with open ("estudiante.txt","w") as archivo:
            for est in self.estudiantes:
                archivo.write(est.mostrar_info() + "\n")  
        print("Archivo guardado correctamente")
        
    def estadisticas(self):

        aprobados = 0
        reprobados = 0

        for est in self.estudiantes:

            if est.nota >= 3:
                aprobados += 1
            else:
                reprobados += 1

        print("\n===== ESTADISTICAS =====")
        print(f"Aprobados: {aprobados}")
        print(f"Reprobados: {reprobados}")                                 
        
        
    def menu(self):
        
        while True:
            print("""
                  =========Menu=========
                  1. registar estudiante
                  2. mostrar estudiante
                  3. buscar estudiante
                  4. eliminar estudiante
                  5. actualizar nota
                  6. calcular promedio
                  7. Guardar estudiantes en archivo
                  8. Estadisticas
                  9. Salir
                  ======================
                  """)
            
            opcion = input ("seleccione una opcion: ")
            if opcion == "1":
                self.registrar_estudiante()

            elif opcion == "2":
                self.mostrar_estudiantes()
                
            elif opcion == "3":
                self.buscar_estudiante()
                
            elif opcion == "4":
                self.eliminar_estudiante()
                
            elif opcion == "5":
                self.actualizar_nota()  
                
            elif opcion == "6":
                self.calcular_promedio()  
                
            elif opcion == "7":
                self.guardar_archivo() 
            
            elif opcion == "8":
                self.estadisticas()     
                        
            elif opcion == "9":
                print("saliendo del sistema") 
                break
            else:
                print("opcion invalida ")
                
                
sistema=SistemaEstudiantes()
sistema.menu()                   
                
        
                        
                
                
                
                           
        
                        
        
        
    
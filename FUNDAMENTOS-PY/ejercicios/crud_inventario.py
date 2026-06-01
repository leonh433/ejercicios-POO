class Producto:
    def __init__(self,codigo,nombre,precio,cantidad,categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        
    def mostrar_info(self):
        return f"codigo: {self.codigo} nombre: {self.nombre} precio: {self.precio} cantidad: {self.cantidad} categoria: {self.categoria}"
    
    
class SistemaInventario:
    def __init__(self):
        self.productos =[]
        
    def registrar_producto(self):
        codigo = input("codigo del producto: ")
        
        if codigo == "":
            print("el codigo no puede estar vacio")
            return
        
        for pro in self.productos:
            if pro.codigo == codigo:
                print("error : el codigo ya existe")
                return
                
        nombre = input("nombre del producto: ")
        
        if nombre == "":
            print("el nombre no puede estar vacio")
            return
            
        while True:
            precio = float(input("precio del producto: "))
            
            if precio >= 0:
                break
            else:
                print("el precio no puede ser negativo")
                
        while True:
            cantidad = int(input("cantidad disponible: "))
            
            if cantidad >= 0:
                break
            else:
                print("la cantidad no puede ser negativa")
                
        categoria = input("categoria del producto: ")
        
        if categoria == "":
            print("la categoria no puede estar vacia")
            return
                
        nuevo_producto = Producto(codigo,nombre,precio,cantidad,categoria)
        self.productos.append(nuevo_producto)
        print("producto registrado correctamente")
        
        
    def mostrar_productos(self):
        
        if len(self.productos)== 0:
            print("no hay productos registrados")
            
        else:
            print("\n LISTA DE PRODUCTOS")
            
            for pro in self.productos:
                print(pro.mostrar_info())
                
                
    def buscar_producto(self):
        dato_buscar = input("ingrese el codigo o nombre del producto: ")
        
        for pro in self.productos:
            if pro.codigo == dato_buscar or pro.nombre == dato_buscar:
                print("\nProducto encontrado")
                print(pro.mostrar_info())
                return
                
        print("producto no encontrado")
        
        
    def actualizar_producto(self):
        codigo_buscar = input("ingrese el codigo del producto: ")
        
        for pro in self.productos:
            if pro.codigo == codigo_buscar:
                
                while True:
                    nuevo_precio = float(input("ingrese nuevo precio: "))
                    
                    if nuevo_precio >= 0:
                        pro.precio = nuevo_precio
                        break
                    else:
                        print("precio invalido")
                        
                while True:
                    nueva_cantidad = int(input("ingrese nueva cantidad: "))
                    
                    if nueva_cantidad >= 0:
                        pro.cantidad = nueva_cantidad
                        break
                    else:
                        print("cantidad invalida")
                        
                nueva_categoria = input("ingrese nueva categoria: ")
                
                if nueva_categoria != "":
                    pro.categoria = nueva_categoria
                    
                print("producto actualizado correctamente")
                return
                
        print("producto no encontrado")
        
        
    def eliminar_producto(self):
        codigo_eliminar = input("ingrese el codigo del producto a eliminar: ")
        
        for pro in self.productos:
            if pro.codigo == codigo_eliminar:
                self.productos.remove(pro)
                print("producto eliminado correctamente")
                return
                
        print("producto no encontrado")
        
        
    def calcular_total_inventario(self):
        if len(self.productos)== 0:
            print("no hay productos registrados")
            return
            
        total = 0
        
        for pro in self.productos:
            total += pro.precio * pro.cantidad
            
        print(f"\nvalor total del inventario: {total}")
        
        
    def mostrar_agotados(self):
        agotados = 0
        
        print("\nPRODUCTOS AGOTADOS")
        
        for pro in self.productos:
            if pro.cantidad == 0:
                print(pro.mostrar_info())
                agotados += 1
                
        if agotados == 0:
            print("no hay productos agotados")
            
            
    def guardar_archivo(self):
        with open("productos.txt","w") as archivo:
            for pro in self.productos:
                archivo.write(pro.mostrar_info() + "\n")
                
        print("archivo guardado correctamente")
        
        
    def menu(self):
        
        while True:
            print("""
                  =========Menu=========
                  1. registrar producto
                  2. mostrar productos
                  3. buscar producto
                  4. actualizar producto
                  5. eliminar producto
                  6. calcular total inventario
                  7. mostrar productos agotados
                  8. guardar productos en archivo
                  9. salir
                  ======================
                  """)
                  
            opcion = input("seleccione una opcion: ")
            
            if opcion == "1":
                self.registrar_producto()
                
            elif opcion == "2":
                self.mostrar_productos()
                
            elif opcion == "3":
                self.buscar_producto()
                
            elif opcion == "4":
                self.actualizar_producto()
                
            elif opcion == "5":
                self.eliminar_producto()
                
            elif opcion == "6":
                self.calcular_total_inventario()
                
            elif opcion == "7":
                self.mostrar_agotados()
                
            elif opcion == "8":
                self.guardar_archivo()
                
            elif opcion == "9":
                print("saliendo del sistema")
                break
                
            else:
                print("opcion invalida")
                
                
sistema = SistemaInventario()
sistema.menu()
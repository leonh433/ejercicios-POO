class Usuario:

    def __init__(self, documento, nombre, correo, rol, estado):

        self.documento = documento
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.estado = estado

    def mostrar_info(self):

        return f"""
Documento: {self.documento}
Nombre: {self.nombre}
Correo: {self.correo}
Rol: {self.rol}
Estado: {self.estado}
"""


class SistemaUsuarios:

    def __init__(self):

        self.usuarios = []

    def registrar_usuario(self):

        documento = input("Ingrese el documento: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")
        rol = input("Ingrese el rol (Administrador, Aprendiz, Instructor): ")
        estado = input("Ingrese el estado (Activo/Inactivo): ")

        if documento == "" or nombre == "" or correo == "" or rol == "" or estado == "":
            print("No se permiten campos vacios")
            return

        existe = False

        for usuario in self.usuarios:

            if usuario.documento == documento:
                existe = True

        if existe == True:
            print("El documento ya existe")
            return

        if "@" not in correo or "." not in correo:
            print("Correo invalido")
            return

        roles = ["Administrador", "Aprendiz", "Instructor"]

        if rol not in roles:
            print("El rol no existe")
            return

        if estado != "Activo" and estado != "Inactivo":
            print("Estado invalido")
            return

        nuevo_usuario = Usuario(documento, nombre, correo, rol, estado)

        self.usuarios.append(nuevo_usuario)

        print("Usuario registrado correctamente")

    def mostrar_usuarios(self):

        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
            return

        for usuario in self.usuarios:

            print(usuario.mostrar_info())

    def buscar_usuario(self):

        opcion = input("""
1. Buscar por documento
2. Buscar por correo
Seleccione una opcion:
""")

        if opcion == "1":

            documento = input("Ingrese el documento: ")

            encontrado = False

            for usuario in self.usuarios:

                if usuario.documento == documento:

                    print(usuario.mostrar_info())
                    encontrado = True

            if encontrado == False:
                print("Usuario no encontrado")

        elif opcion == "2":

            correo = input("Ingrese el correo: ")

            encontrado = False

            for usuario in self.usuarios:

                if usuario.correo == correo:

                    print(usuario.mostrar_info())
                    encontrado = True

            if encontrado == False:
                print("Usuario no encontrado")

        else:

            print("Opcion invalida")

    def actualizar_usuario(self):

        documento = input("Ingrese el documento del usuario: ")

        encontrado = False

        for usuario in self.usuarios:

            if usuario.documento == documento:

                encontrado = True

                nombre = input("Ingrese el nuevo nombre: ")
                correo = input("Ingrese el nuevo correo: ")
                rol = input("Ingrese el nuevo rol: ")
                estado = input("Ingrese el nuevo estado: ")

                if nombre == "" or correo == "" or rol == "" or estado == "":
                    print("No se permiten campos vacios")
                    return

                if "@" not in correo or "." not in correo:
                    print("Correo invalido")
                    return

                roles = ["Administrador", "Aprendiz", "Instructor"]

                if rol not in roles:
                    print("El rol no existe")
                    return

                if estado != "Activo" and estado != "Inactivo":
                    print("Estado invalido")
                    return

                usuario.nombre = nombre
                usuario.correo = correo
                usuario.rol = rol
                usuario.estado = estado

                print("Usuario actualizado correctamente")

        if encontrado == False:
            print("Usuario no encontrado")

    def eliminar_usuario(self):

        documento = input("Ingrese el documento del usuario: ")

        encontrado = False

        for usuario in self.usuarios:

            if usuario.documento == documento:

                self.usuarios.remove(usuario)

                encontrado = True

                print("Usuario eliminado correctamente")

        if encontrado == False:
            print("Usuario no encontrado")

    def mostrar_activos(self):

        encontrado = False

        for usuario in self.usuarios:

            if usuario.estado == "Activo":

                print(usuario.mostrar_info())

                encontrado = True

        if encontrado == False:
            print("No hay usuarios activos")

    def contar_roles(self):

        administradores = 0
        aprendices = 0
        instructores = 0

        for usuario in self.usuarios:

            if usuario.rol == "Administrador":
                administradores += 1

            elif usuario.rol == "Aprendiz":
                aprendices += 1

            elif usuario.rol == "Instructor":
                instructores += 1

        print(f"Administradores: {administradores}")
        print(f"Aprendices: {aprendices}")
        print(f"Instructores: {instructores}")

    def guardar_archivo(self):

        archivo = open("usuarios.txt", "w")

        for usuario in self.usuarios:

            archivo.write(usuario.mostrar_info())
            archivo.write("\n-----------------\n")

        archivo.close()

        print("Datos guardados correctamente")


sistema = SistemaUsuarios()

while True:

    opcion = input("""
========== MENU ==========
1. Registrar usuario
2. Mostrar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Mostrar usuarios activos
7. Contar usuarios por rol
8. Guardar archivo
9. Salir

Seleccione una opcion:
""")

    if opcion == "1":

        sistema.registrar_usuario()

    elif opcion == "2":

        sistema.mostrar_usuarios()

    elif opcion == "3":

        sistema.buscar_usuario()

    elif opcion == "4":

        sistema.actualizar_usuario()

    elif opcion == "5":

        sistema.eliminar_usuario()

    elif opcion == "6":

        sistema.mostrar_activos()

    elif opcion == "7":

        sistema.contar_roles()

    elif opcion == "8":

        sistema.guardar_archivo()

    elif opcion == "9":

        print("Saliendo del sistema")
        break

    else:

        print("Opcion invalida")

def validar_nombre(nombre):
    if len(nombre) == 0:
        return False
    
    solo_espacios = True
    for caracter in nombre:
        if caracter != " ":
            solo_espacios = False
            
    if solo_espacios == True:
        return False
        
    return True


def validar_edad(edad):
    if edad > 0:
        return True
    return False


def validar_nota(nota):
    if nota >= 1.0 and nota <= 7.0:
        return True
    return False



def mostrar_menu():
    print("=== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")


def pedir_opcion():
    opcion_valida = False
    opcion_elegida = 0
    
    while opcion_valida == False:
        try:
            opcion_elegida = int(input("Seleccione una opción (1-6): "))
            if opcion_elegida >= 1 and opcion_elegida <= 6:
                opcion_valida = True
            else:
                print("Opción fuera de rango. Por favor elija un número del 1 al 6.")
                print()
        except:
            print("Error: Por favor, ingrese un número entero válido.")
            print()
            
    return opcion_elegida

def buscar_estudiante(lista_estudiantes, nombre_buscar):
    posicion = 0
    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre_buscar:
            return posicion
        posicion = posicion = 1
    return -1

def actualizar_estados(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False


def agregar_estudiante(lista_estudiantes):
    print()
    print("--- REGISTRAR NUEVO ESTUDIANTE ---")
    
    nombre_correcto = False
    nombre = ""
    while nombre_correcto == False:
        nombre = input("Ingrese el nombre completo del estudiante: ")
        if validar_nombre(nombre) == True:
            nombre_correcto = True
        else:
            print("Error: El nombre no puede estar vacío ni contener solo espacios.")
            print()
            
    edad_correcta = False
    edad = 0
    while edad_correcta == False:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if validar_edad(edad) == True:
                edad_correcta = True
            else:
                print("Error: La edad debe ser un número entero mayor que cero.")
                print()
        except:
            print("Error: Debe ingresar un número entero válido para la edad.")
            print()
            
    nota_correcta = False
    nota = 0.0
    while nota_correcta == False:
        try:
            nota = float(input("Ingrese la nota de la asignatura (1.0 - 7.0): "))
            if validar_nota(nota) == True:
                nota_correcta = True
            else:
                print("Error: La nota debe ser un número decimal entre 1.0 y 7.0.")
                print()
        except:
            print("Error: Debe ingresar un número decimal válido (use punto para decimales).")
            print()

    nuevo_registro = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,s
        "aprobado": False 
    }
    
    lista_estudiantes.append(nuevo_registro)
    print("¡Estudiante registrado de forma exitosa!")

def ejecutar_busqueda(lista_estudiante):
    print()
    print("--- Buscar estudiante ---")
    nombre_buscar = input("Ingres el nombre del estudiante que esta buscando: ")

    posicion = buscar_estudiante(lista_estudiantes, nombre_buscar)

    if posicion != -1:
        estudiante = lista_estudiantes[posicion]
        print("Estudiante encontrado en la posicion:", posicion)
        print("Nombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Nota:", estudiante["nota"])
        if estudiante["Aprobado"] == True:
            print("Estado: APROBADO")
        else:
            print("Estado: DESAPROBADO")
    else:
        print("El estudiante no se encuentra registrado.")


def eliminar_estudiante(lista_estudiantes):
    print()
    print("--- Eliminar estudiante ---")
    nombre_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")

    posicion = buscar_estudiante(lista_estudiantes, nombre_eliminar)

    if posicion != -1:
        lista_estudiantes.pop(posicion)
        print("El estudiante ", nombre_eliminar, "ha sido eliminado correctamente")
    else:
        print("El estudiante ", nombre_eliminar, "no se encuentra en registrado en el sistema")


def mostrar_estudiantes(lista_estudiantes):
    print()

    actualizar_estados(lista_estudiantes)
    
    print("=== LISTA DE ESTUDIANTES ===")
    
    if len(lista_estudiantes) == 0:
        print("La lista está vacía. No hay estudiantes registrados.")
    else:
        for estudiante in lista_estudiantes:
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Nota:", estudiante["nota"])
            

            if estudiante["aprobado"] == True:
                print("Estado: APROBADO")
            else:
                print("Estado: REPROBADO")
            print("****")


coleccion_general = []
programa_activo = True

while programa_activo == True:
    print()
    mostrar_menu()      
    opcion = pedir_opcion() 
    
    if opcion == 1:
        agregar_estudiante(coleccion_general)
        
    elif opcion == 2:
        ejecutar_busqueda(coleccion_general)
        
    elif opcion == 3:
        eliminar_estudiante(coleccion_general)
        
    elif opcion == 4:
        print()
        actualizar_estados(coleccion_general)
        print("¡Estados de aprobación sincronizados de forma manual!")
        
    elif opcion == 5:
        mostrar_estudiantes(coleccion_general)
        
    elif opcion == 6:
        print()
        print("Gracias por usar el sistema. Vuelva Pronto")
        programa_activo = False

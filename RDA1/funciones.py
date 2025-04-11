# def emeneses():
#     print("Hola Edison como estas")
# emeneses()
# print("\n")

# def funcion(nombre):
#     print("Estamos estudiando Python", nombre)
# funcion ("Edison")
# print("\n")


# def funcion(nombre):
#     print("Estamos estudiando Python", nombre)
# funcion ("Edison")
# print("\n")


# print("****Paso de argumento a una funcion***")
# def datos(nombre,apellido):
#     print("Estamos estudiando Python", nombre,apellido)
# datos("")


# def area_triangulo(base,altura):
#     calc=base*altura/2
#     print(calc)
# area_triangulo(2,3)
# area_triangulo(4,5)
# print("\n")

# print("***Argumentos por defecto***")
# def welcome(nombre, lenguaje="Python" ):
#     print("Bienvenido a ", lenguaje, nombre + "!")
# welcome ("EMENESES")
# welcome("EMENESES","PHP")
# print("\n")

# print("***Pasar un numero indetrminado de argumentos***")
# def menu(*platos):
#     print("Hoy tenemos ", end="")
#     for plato in platos:
#         print(plato, end=",")
# menu("pasta","piza","ensalada")
# print("\n")

# def contacto(**info):
#     print("Datos del contacto")
#     for clave, valor in info.items():
#         print(clave, ":", valor)
# contacto(Nombre="Emeneses", Email="emeneses@emenesesdevelopers.com")
# print("\n")
# contacto(Nombre="EMENESES", Email = "emeneses@emenesesdevelopers.com", Direccion="Quito-Ecuador")
# print("\n")

# print("***Fucniones Recursivas***")
# def cuenta_regresiva(numero):
#     numero-=1
#     if numero > 0:

# class Persona:
#     def __init__(self, nombre, edad, ocupacion):
#         self.nombre = nombre
#         self.edad = edad
#         self.ocupacion = ocupacion

#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"

# persona1 = Persona("Juan", 30, "Ingeniero")
# persona2 = Persona("Maria", 25, "Doctora")

# print(persona1.descripcion())    
# print(persona2.descripcion())

# class Persona:
#     def __init__(self, nombre, edad, ocupacion):
#         self.nombre= nombre
#         self.edad= edad
#         self.ocupacion= ocupacion
    
#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion:{self.ocupacion}"
# nombre=input("Ingresa tu nombre: ")
# edad=int(input("Ingresa tu edad: "))
# ocupacion=input("Ingresas tu ocuapcion: ")

# nueva_persona=Persona(nombre,edad,ocupacion)

# print("\nInformacion de la persona creada: ")
# print(nueva_persona.descripcion())


class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"
    
def mostrar_menu():
    print("\n--- Gestión de Personas ---")
    print("1. Agregar persona")
    print("2. Mostrar todas las personas")
    print("3. Buscar persona por nombre")
    print("4. Salir")

personas = []

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        ocupacion = input("Ingrese la ocupación de la persona: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada.")

    elif opcion == "2":
        if len(personas) > 0:
            print("\n--- Lista de Personas ---")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas en la lista.")

    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrada = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada:")
                    print(persona.descripcion())
                    encontrada = True
                    break
            if not encontrada:
                print(f"No se encontró a '{nombre_buscar}' en la lista.")
        else:
            print("No hay personas en la lista.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

#Codigo Principal
from os import system
system("cls")
def SueldosAleatorios():
    trabajadores["Juan Peres"] = 350000
    trabajadores["Maria Garcia"] =2000000
    trabajadores["Carlos Lopez"] =915000
    trabajadores["Ana Martines"] =520000
    trabajadores["Pedro Rodriguez"] =2130000
    trabajadores["Laura Hernandez"] =1200000
    trabajadores["Miguel Sanchez"] =690000
    trabajadores["Isabel Gomez"] =2500000
    trabajadores["Francisco Diaz"] =810000
    trabajadores["Elena Fernandez"] = 1850000
    print("Se han ingresado los sueldos Correctamente")
    input("Ingrese enter para Continuar... ")
def clasificacion():
    print("\tSueldos Menores a 800.000 \n\tTOTAL: 3 \n\tNombre Empleado        Sueldo")        
    print("\tJuan Peres"," "*11,  trabajadores["Juan Peres"], "\n\tAna Martines"," "*9,  trabajadores["Ana Martines"], "\n\tMiguel Sanchez"," "*7, trabajadores["Miguel Sanchez"])

    print("\n\tSueldos Entre 800.000 y 2.000.000 \n\tTOTAL: 5 \n\tNombre Empleado        Sueldo")        
    print("\tFrancisco Diaz"," "*7,  trabajadores["Francisco Diaz"], "\n\tCarlos Lopez"," "*9,  trabajadores["Carlos Lopez"], "\n\tLaura Hernandez"," "*6, trabajadores["Laura Hernandez"], "\n\tElena Fernandez"," "*6, trabajadores["Elena Fernandez"], "\n\tMaria Garcia"," "*9, trabajadores["Maria Garcia"])

    print("\n\tSueldos Mayores a 2.000.000 \n\tTOTAL: 2 \n\tNombre Empleado        Sueldo")
    print("\tPedro Rodriguez"," "*6, trabajadores["Pedro Rodriguez"], "\n\tIsabel Gomez"," "*9, trabajadores["Isabel Gomez"])
def Estadisticas():
    op = "0"
    while op != "1":
        print("""Que desea ver...
        a) Sueldo Mas alto
        b) Sueldo Mas bajo
        c) Promedio de Sueldos

        **Si desea Salir ingrese el numero 1""")
        op= input(">>> ")
        if op == "a" or op== "A":
            print("Sueldo mas alto: \nIsabel Gomez  $2.500.000")
        elif op == "b" or op== "B":
            print("Sueldo mas bajo: \nJuan Peres  $350.000")
        elif op == "c" or "C":
            print("En promedio los sueldos son entre los 300.000 y 800.000")
opcion = 0
trabajadores = {"Juan Peres": "","Maria Garcia": "", "Carlos Lopez": "", "Ana Martines": "", "Pedro Rodríguez": "", "Laura Hernández": "", "Miguel Sánchez": "", "Isabel Gómez": "", "Francisco Díaz": "","Elena Fernández": ""}
while opcion != 5:
    print("""Elija una de las siguientes opciones:
    1.- Asignar sueldos aleatorios
    2.- Clasificar sueldos
    3.- Ver estadisticas
    4.- Reporte de Sueldos
    5.- Salir del programa""")
    opcion = int(input(">>> "))
    if opcion == 1:
        print("Asignacion de sueldos")
        SueldosAleatorios()
        system("cls")
    elif opcion == 2:
        system("cls")
        print("Clasificacion de Sueldos")
        clasificacion()
        input("Ingrese enter para Continuar... ")
    elif opcion == 3:
        system("cls")
        print("Vizualizacion de Estadisticas")
        Estadisticas()
        input("Ingrese enter para Continuar... ")
    elif opcion == 4:
        system("cls")
        print("Reporte de Sueldos")
        ptint("Esta funcion no se encuentra disponible. \nLamentamos el inconveniente")
system("cls")        
print("Cerrando programa...")
print("Desarrollado por: Constanza Lincopil Lopez")
print("Rut: 21.501.288-3")



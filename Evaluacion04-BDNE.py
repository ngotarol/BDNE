
from modelo import(ConsultarDocumento, RevisarBase,CrearColeccion,InsertarDocumento,RevisarCol)
import json

eleccion = """_________________________________
Bienvenido al menú.
Seleccione una opción:

1 - Crear base de datos
2 - Crear coleccion
3 - Insertar documento
4 - Eliminar documento (no hecho)
5 - Modificar documento (no hecho)
6 - Consultar documento 
_________________________________
"""

submenu = """_________________________________
1. Consultar por campo principal
2. Consultar por algún campo en particular
_________________________________"""

opcion = 1
while opcion > 0 and opcion < 7:
    print(eleccion)
    opcion = int(input("Ingrese una opción \n"))
    if opcion == 1:
        base = input("\nIngresar nombre de la base de datos \n")
        resultado = RevisarBase(base)
        if resultado:
            print("Base de datos ya existe")
        else:
            coleccion = input("\nIngresar nombre de la coleccion \n")
            CrearColeccion(base,coleccion)
    elif opcion == 2:
        base = input("\nEn qué base de datos desea crear la colección? \n")
        resultado = RevisarBase(base)
        if resultado: 
            coleccion = input("\nIngrese el nombre de la coleccion \n")
            CrearColeccion(base,coleccion)
        else:
            print("Base de datos no existe, debe crearla")        
    elif opcion == 3:
        bc = input("\nEn qué base de datos y coleccion desea insertar el documento? formato: base,coleccion\n").split(',')
        base = bc[0]
        coleccion = bc[1]
        resultado1 = RevisarBase(base)
        resultado2 = RevisarCol(base, coleccion)
        if resultado1:
            if resultado2:
                filename = input("Ingrese el nombre del archivo a insertar\n")
                archivo = open(filename)
                anidado = json.load(archivo)
                InsertarDocumento(base,coleccion,anidado)
            else:
                print("Coleccion no existe, debe crearla")  
        else:
            print("Base de datos no existe, debe crearla")
    elif opcion == 6:
            bc = input("\nEn qué base de datos y coleccion desea consultar el documento? formato: base,coleccion\n").split(',')
            base = bc[0]
            coleccion = bc[1]
            resultado1 = RevisarBase(base)
            resultado2 = RevisarCol(base, coleccion)
            if resultado1:
                if resultado2:
                    print(submenu)
                    subopcion = int(input("Ingrese una opción \n"))
                    if subopcion == 1:
                        valor = input("Ingrese el id del documento a consultar\n")
                        ConsultarDocumento(base,coleccion,"_id",valor)
                    elif subopcion ==2:
                        bc = input("\nIngrese el campo y valor por el que desea consultar\n").split(',')
                        campo = bc[0]
                        valor = bc[1]
                        ConsultarDocumento(base,coleccion,campo,valor)
                else:
                    print("Coleccion no existe, debe crearla") 
            else:
                print("Base de datos no existe, debe crearla")             
else:
    print("Ha salido del programa")
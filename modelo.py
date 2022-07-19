import json
import pymongo
from bson.objectid import ObjectId


def Conexion():
    cliente = pymongo.MongoClient("localhost",27017)
    return cliente

def RevisarBase(base):
    lista = Conexion().list_database_names()
    if base in lista:
        return True
    else:        
        return False

def RevisarCol(base,coleccion):
    lista = Conexion().get_database(base).list_collection_names()
    if coleccion in lista:
        return True
    else:        
        return False

def CrearColeccion(base,coleccion):   
    if RevisarBase(base)!= True:
        Conexion()[base]   

    db = Conexion().get_database(base)
    if coleccion in db.list_collection_names():
        print("Coleccion ya existe")
        return False
    else:
        db.create_collection(coleccion)
        print(f"Se creó la coleccion: {coleccion} en la base {base}") 
        return  True
    
def InsertarDocumento(base,coleccion,jaison):
    a = Conexion().get_database(base).get_collection(coleccion)
    if type(jaison) is dict:
        a.insert_one(jaison)        
        print(a.find())
    else :
        a.insert_many(jaison)
        print(a.find())

def ConsultarDocumento(base,coleccion,texto,valor):
    a = Conexion().get_database(base).get_collection(coleccion)
    if texto == "_id":
        resultado = (a.find_one({texto:valor}))
        print(resultado)
    else:
        resultado = a.find({texto:valor})
        for x in resultado:
            print(x)



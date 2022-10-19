from modulo.py import *

def test_lee_entrenos(datos):
    print("\nNúmero de registros guardados:", len(datos))
    print("\nLos dos primeros registros son:", datos[:2])
    print("\nLos tres últimos registros son:", datos[-3:])
    

def test_filtrar_por_ubicacion(datos, location):
    print("\nLos entrenos que se realizan en ", location, " son:\n")
    print(filtrar_por_ubicacion(datos, location))

def test_obtiene_distintos_tipos(datos):
    print("Los distintos tipos de entreno que hay son:\n", obtiene_distintos_tipos(datos))


datos=lee_entrenos("data/entrenos.csv")

test_lee_entrenos(datos)
test_filtrar_por_ubicacion(datos, "Sevilla") 
test_obtiene_distintos_tipos(datos)
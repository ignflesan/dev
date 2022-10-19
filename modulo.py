import csv
from datetime import datetime


Entreno=namedtuple("entreno", "tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido" )

def comparte(a):
    res=False
    if a=="S"
        res=True
    return res


def lee_entrenos(fichero):
    res=list
    with open (fichero, encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            res.append(Entreno(tipo, datetime.strptime(fechahora, "%d/%m/%Y %H:%M"), ubicacion,duracion,calorias,distancia,frecuencia, comparte(compartido)))
    return res
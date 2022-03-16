from enum import Enum

# Enumeración Eps
class Eps(Enum):
    ASMETSALUD = "Asmet Salud"
    SURA = "Sura"
    MEDIMAS = "Medimas"
    SALUDMORTAL = "Salud Mortal"

# Enumeración RH
class Rh(Enum):
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B-'
    B_NEGATIVE = 'B+'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'

class User: 
    def __init__(self, nombre:str, apellido:str, cc:str, edad:int, rh:Rh, eps:Eps):
        self.__nombre = nombre    
        self.__apellido = apellido
        self.__cc = cc
        self.__edad = edad
        self.__rh = rh
        self.__Eps = eps
        
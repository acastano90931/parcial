class Nodo (object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
        
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    def insertar(self, dato):
        nodo = Nodo(dato)

        if  self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza

        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
    def iterar(self):
        actual = self.cabeza
    
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(int(input("Ingrese un número: ")))
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)

print()

numeros.insertar(int(input("Ingrese un número: ")))

print('Cantidad actual de elementos:', numeros.contador)

print()


for d in numeros.iterar():
    print(d)





















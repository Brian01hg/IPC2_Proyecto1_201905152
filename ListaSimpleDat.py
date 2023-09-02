from Datoo import Datoo
from graphviz import Digraph
class ListaSimpleDato():
    def __init__(self):
        self.inicio = None

    def insertar(self,dato):
        nuevo = Datoo(dato)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    def binaria(self):
        tmp = self.inicio
        while tmp is not None:
            if str(tmp.dato) != 0:
                nuevo = str(tmp.dato).replace(str(tmp.dato), '1')
                print(nuevo)
            else:
                print(0)
            tmp = tmp.siguiente

    def imprimir(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(tmp.dato))
            contador += 1
            tmp = tmp.siguiente
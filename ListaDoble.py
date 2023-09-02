from Clase import  Clase
class ListaDoble:
    def __init__(self):
        self.inicio = None

    def añadir(self, x, y, dato):
        nuevo = Clase(x, y, dato)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
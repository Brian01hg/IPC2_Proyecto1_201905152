from dato import Dato
class ListaSimple():
    def __init__(self):
        self.inicio = None

    def añadir(self, t, A):
        nuevo = Dato(t, A)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def imprimir(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(tmp.t), str(tmp.A))
            contador +=1
            tmp = tmp.siguiente

class Senal:
    def __init__(self, nombre, t, A):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.datos = [[0] * A for _ in range(t)]
        self.matriz_reducida = []
        self.matriz_elem = None

    def agregar_dato(self, t, A, valor):
        self.datos[t-1][A-1] = valor

    def obtener_dato(self, t, A):
        return self.datos[t-1][A-1]
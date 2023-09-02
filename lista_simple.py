import xml.etree.ElementTree as ET
from nodo import Senal
class ProcesadorSenales:
    def __init__(self):
        self.senales = []

    def cargar_senales(self, nombre_archivo):
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

        for senal_elem in root.findall('senal'):
            nombre = senal_elem.get('nombre')
            t = int(senal_elem.get('t'))
            A = int(senal_elem.get('A'))

            senal = Senal(nombre, t, A)
            for dato_elem in senal_elem.findall('dato'):
                tiempo = int(dato_elem.get('t'))
                amplitud = int(dato_elem.get('A'))
                valor = int(dato_elem.text)
                senal.agregar_dato(tiempo, amplitud, valor)

            self.senales.append(senal)

    def procesar_senales(self):
        for senal in self.senales:
        # Crear un diccionario para almacenar los grupos
            grupos = {}

        # Recorrer cada fila de la matriz de datos de la señal
        for t in range(senal.t):
            # Obtener el patrón de frecuencias para la fila actual
            patron = tuple(senal.obtener_dato(t, A) for A in range(senal.A))

            # Si el patrón ya está en un grupo, agregar el tiempo a ese grupo
            if patron in grupos:
                grupos[patron].append(t + 1)
            else:
                # Si no está en un grupo, crear un nuevo grupo con el patrón
                grupos[patron] = [t + 1]

        # Crear una lista para la matriz reducida
        matriz_reducida = []

        # Generar la matriz reducida a partir de los grupos
        for patron, tiempos in grupos.items():
            fila_reducida = [sum(senal.obtener_dato(t - 1, A) for t in tiempos) for A in range(senal.A)]
            matriz_reducida.append((patron, tiempos, fila_reducida))

        # Almacenar la matriz reducida en la instancia de Senal
        senal.matriz_reducida = matriz_reducida

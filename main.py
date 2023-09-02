import xml.etree.ElementTree as ET
from graphviz import Digraph
from tkinter import *
from tkinter.filedialog import askopenfile


while seleccion != 6:
    print("""       Menu Principal
                1. Cargar Archivo
                2. Procesar Archivo
                3. Escribir Archivo de Salida
                4. Mostrar Datos del Estudiante
                5. Generar Grafica
                6. Salida
            """)
    seleccion = input()
    if seleccion == "1":
        Tk().withdraw()
        archivo = askopenfile(mode='r', filetypes=[('Xml Files', '*.xml''')])
        archivo = open("entrada.xml", "r")
        tree = ET.parse(archivo)
        root = tree.getroot()
        
    elif seleccion == "2":
        print("matriz binaria")
    elif seleccion == "3":
        print("")

    elif seleccion == "4":
        print("""
        Brian Antonio Hernandez Gil
        201905152
        Introduccion a la Programacion y Computacion 2 Seccion D
        Ingenieria en Ciencias y Sistemas
        4to Semestre
        """)
    elif  seleccion == "5":
        nombre_matriz = input('Escriba la matriz que desea graficar:  ')
        for elemento in root:
            dot = Digraph(comment='The Round Table')
            dot.node('A', nombre_matriz)
            if nombre_matriz == elemento.attrib['nombre']:
                dot.node('B', 't= ' + elemento.attrib['t'])
                dot.node('C', 'A= ' + elemento.attrib['A'])
                dot.edges(['AB','AC'])
                print(dot.source)
                print(dot.node)
               
        else:
            print("No se encuentra dicha matriz en el archivo")
            print("Intentalo denuevo")
            
    elif seleccion == 6:
        print("Saliendo del programa...")
        break

    else:
         print("Opción inválida. Intente nuevamente.")


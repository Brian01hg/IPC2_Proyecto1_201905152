import xml.etree.ElementTree as ET
from lista_simple import ProcesadorSenales
from ListaSimpleDat import ListaSimpleDato
from ListaSimple import ListaSimple
import time


def main():
    procesador = ProcesadorSenales()
    

    while True:
        print("Menú:")
        print("1. Cargar Archivo")
        print("2. Procesar Señales")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Gráfico")
        print("6. Salir")

        opcion = input("Ingrese su elección: ")

        if opcion == '1':
            nombre_matriz = input("Ingrese el nombre del archivo de entrada: ")
            procesador.cargar_senales(nombre_matriz)
        elif opcion == '2':
            procesador.procesar_senales()
            time.sleep(1)
            print("Calculando la matriz binaria...")
            time.sleep(1)
            for i in range(5):
                d = "███████████"
                print("█"+ d)
                time.sleep(0.7)
            time.sleep(2)
            print("Realizando suma de tuplas...")
            time.sleep(2)
            print("Realizado con exito")
        elif opcion == '3':
            nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ")
            procesador.procesar_senales()
            nombre_xml = nombre_archivo_salida + ".xml"
            procesador.generar_archivo_xml(nombre_xml)
            procesador.graficar_matriz_reducida(nombre_archivo_salida + ".png")

        elif opcion == '4':
            
            print("""
                Brian Antonio Hernandez Gil
                201905152
                Introduccion a la Programacion y Computacion 2 Seccion D
                Ingenieria en Ciencias y Sistemas
                4to Semestre
                    """)
            pass
        elif opcion == '5':
            nombre_matriz = input("Ingrese el nombre de la señal: ")
            procesador.generar_grafico(nombre_matriz)
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")
        

if __name__ == "__main__":
    main()
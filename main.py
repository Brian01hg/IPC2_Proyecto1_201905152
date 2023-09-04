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

            root_salida = ET.Element('senalesReducidas')

            for senal in procesador.senales:
                senal_elem = ET.SubElement(root_salida, 'senal', nombre=senal.nombre, A=str(senal.A))

            for g, (patron, tiempos, fila_reducida) in enumerate(senal.matriz_reducida):
                grupo_elem = ET.SubElement(senal_elem, 'grupo', g=str(g + 1))
                tiempos_elem = ET.SubElement(grupo_elem, 'tiempos')
                tiempos_elem.text = ','.join(map(str, tiempos))

                datos_grupo_elem = ET.SubElement(grupo_elem, 'datosGrupo')

            for A, valor in enumerate(fila_reducida):
                dato_elem = ET.SubElement(datos_grupo_elem, 'dato', A=str(A + 1))
                dato_elem.text = str(valor)

                tree_salida = ET.ElementTree(root_salida)
                tree_salida.write(nombre_archivo_salida)

                print(f"Archivo de salida '{nombre_archivo_salida}' creado exitosamente.")
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
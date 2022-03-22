from functions import clear
from Comida import *

def gestionComida(data):

    while True:
        clear()
        print('******************************')
        print('       GESTIÓN DE FERIA')
        print('******************************\n')
        
        print('¿Qué desea hacer?\n')
        print('===>Eliminar producto (1)')
        print('===>Buscar productos (2)')
        print('===>Menú principal (3)')
        opcion = input('===>Opción: ')

        if opcion == '1':
            continue
        elif opcion == '2':
            print('¿Qué filtro desea aplicar?\n')
            print('===>Nombre (1)')
            print('===>Tipo (2)')
            print('===>Rango de precio (3)')
            opcion = input('===>Opción: ')

            clear()

            if opcion == '1':
                nombre = input('Ingrese nombre del producto: ')
                for producto in data:
                    if nombre.lower() == producto.nombre.lower():
                        producto.info()
            elif opcion == '2':
                tipo = input('Ingrese el tipo de comida (bebida) (alimento): ')
                for producto in data:
                    if tipo.lower() == producto.clasificacion.lower():
                        producto.info()
            elif opcion == '3':
                min = int(input('Ingrese el menor precio: $'))
                max = int(input('Ingrese el mayor precio: $'))
                for producto in data:
                    if producto.precio >= min and producto.precio <= max:
                        producto.info()
            else:
                print('opción no válida')
        else:
            break

        ddd= input()

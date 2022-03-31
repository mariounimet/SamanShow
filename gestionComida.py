from functions import clear
from Comida import *

def gestionComida(data):

    while True:
        clear()
        print('******************************')
        print('       GESTIÓN DE FERIA')
        print('******************************\n')
        
        print('¿Qué desea hacer?\n')
        print('===>Eliminar producto del menú(1)')
        print('===>Buscar productos (2)')
        print('===>Menú principal (3)')
        opcion = input('===>Opción: ')

        clear()

        if opcion == '1':
            #Elimina el producto del menú 
            for producto in data:
                print('-',producto.nombre)
            nombre = input('\nEscriba el nombre del producto que desea eliminar: ')
            for producto in data:
                if producto.nombre.lower() == nombre.lower():
                    producto.visible = False
                    break
            print('Producto eliminado del menú')
            input('Presione ENTER para volver al menú principal')

        elif opcion == '2':
            #busca productos de la feria con filtro
            print('¿Qué filtro desea aplicar?\n')
            print('===>Nombre (1)')
            print('===>Tipo (2)')
            print('===>Rango de precio (3)')
            print('===>Regresar (4)')
            opcion = input('===>Opción: ')

            clear()

            if opcion == '1':
                nombre = input('Ingrese nombre del producto: ')
                for producto in data:
                    if nombre.lower() == producto.nombre.lower() and producto.visible:
                        producto.info()
                input('\nPresione ENTER para regresar')
            elif opcion == '2':
                tipo = input('Ingrese el tipo de comida (bebida) (alimento): ')
                for producto in data:
                    if tipo.lower() == producto.clasificacion.lower() and producto.visible:
                        producto.info()
                input('\nPresione ENTER para regresar')
            elif opcion == '3':
                min = int(input('Ingrese el menor precio: $'))
                max = int(input('Ingrese el mayor precio: $'))
                for producto in data:
                    if producto.precio >= min and producto.precio <= max and producto.visible:
                        producto.info()
                input('\nPresione ENTER para regresar')
            elif opcion == '4':
                continue
            else:
                print('opción no válida')
        else:
            break

from Comida import *
from functions import clear

def ventaFeria(comida, clientes):

    clear()
    print('******************************')
    print('        FERIA DE COMIDA')
    print('******************************\n')

    ci = input('-->Introduzca número de cédula: ')
    buscador = False
    numero_clinte = 0
    bolsa = []
    monto = 0

    for cliente in clientes:
        if cliente.ci == ci:
            buscador = True
            break
        numero_clinte += 1
        
    if not buscador:
        return False

    while True:
        clear()
        print('*** Bebidas ***\n')
        for producto in comida:
            if isinstance(producto, Bebida):
                producto.info()
        print('\n*** Alimentos ***\n')
        for producto in comida:
            if isinstance(producto, Alimento):
                producto.info()

        eleccion = input('\nEscriba el nombre del producto que desea: ')
        cantidad = int(input('Cantidad a comprar: '))
        buscador = False
        existencia = True
        precio = 0

        for producto in comida:
            if eleccion.lower() == producto.nombre.lower():
                if producto.cantidad-cantidad < 0:
                    existencia = False
                buscador = True
                precio = producto.precio
                break

        if not buscador:
            print('\nProducto no válido')
            input('Presione ENTER para continuar')
            clear()
            continue
        elif not existencia:
            print('\nNo hay suficientes unidades en inventario')
            input('Presione ENTER para continuar')
            clear()
            continue

        for i in range(cantidad):
            bolsa.append(eleccion.capitalize())
            monto += precio
        

        continuar = input('¿Comprar otro producto? (y) (n)\n===>Opción: ').lower()
        if continuar == 'y':
            continue
        else:
            break

    lista = set(bolsa)

    for producto in lista:
        print(producto, ', ', bolsa.count(producto))
        

    input()


    return True
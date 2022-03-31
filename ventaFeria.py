from Comida import *
from functions import clear, narcisista

def ventaFeria(comida, clientes):

    clear()
    print('******************************')
    print('        FERIA DE COMIDA')
    print('******************************\n')

    ci = input('-->Introduzca número de cédula: ')
    buscador = False
    numero_cliente = 0
    bolsa = []
    monto = 0

    #busca si el cliente ya compró entreda a un evento

    for cliente in clientes:
        if cliente.ci == ci:
            buscador = True
            break
        numero_cliente += 1
        
    if not buscador:
        return False

    #imprime información de las bebidas y alimentos
    while True:
        clear()
        print('*** Bebidas ***\n')
        for producto in comida:
            if isinstance(producto, Bebida) and producto.visible:
                producto.info()
        print('\n*** Alimentos ***\n')
        for producto in comida:
            if isinstance(producto, Alimento) and producto.visible:
                producto.info()

        #escoger el producto y la cantidad del mismo que desee el cliente
        eleccion = input('\nEscriba el nombre del producto que desea: ')
        cantidad = int(input('Cantidad a comprar: '))
        buscador = False
        existencia = True
        precio = 0

        #se verifica si el producto y cantidad son válidos
        for producto in comida:
            if eleccion.lower() == producto.nombre.lower() and producto.visible:
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

        #agrega productos a la bolsa
        for i in range(cantidad):
            bolsa.append(eleccion.lower())
            monto += precio
        

        continuar = input('¿Comprar otro producto? (y) (n)\n===>Opción: ').lower()
        if continuar == 'y':
            continue
        else:
            clear()
            break

    #descuentos y monto total
    descuento = 0

    if narcisista(ci):
        descuento += monto*0.15

    total = round(monto - descuento, 2)
    lista = set(bolsa)

    #imprime productos y monto a pagar
    for producto in lista:
        print(producto, ':', bolsa.count(producto))
    
    print(f'Subtotal: {round(monto, 2)}$')
    print(f'Descuento: {descuento}$')
    print(f'Total: {total}$')

    continuar = input('¿Desea proceder con la compra? (y) (n)\n===>Opción: ').lower()

    if continuar == 'y':
        #agrega productos a la base de datos de vendidos
        with open('vendidos.txt', 'a') as file:
            for i in bolsa:
                file.write(f'{i}|')
        clientes[numero_cliente].montoFeria += total
        for producto in comida:
            if producto.nombre.lower() in lista:
                producto.vender(bolsa.count(producto.nombre.lower()))
    else:
        return False
    print('Compra exitosa')
    input('Presione ENTER para volver al menú principal')
    return True
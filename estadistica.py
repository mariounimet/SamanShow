from functions import clear

def estadistica(clientes, eventos, comida):
    clear()
    print('******************************')
    print('         ESTADÍSTICAS')
    print('******************************\n')
    promGasto = 0
    noFeria = 0

    for cliente in clientes:
        promGasto += cliente.totalMonto()
        if cliente.montoFeria == 0:
            noFeria += 1

    for i in range(len(clientes)-1):
        mayor = clientes[i].totalMonto()
        clienteMayor = i
        for j in range(len(clientes[i:])):
            if clientes[j+i].totalMonto() > mayor:
                mayor = clientes[j+i].totalMonto()
                clienteMayor = j+i
        
        aux = clientes[clienteMayor]
        clientes[clienteMayor] = clientes[i]
        clientes[i] = aux

    for i in range(len(eventos)-1):
        mayor = eventos[i].ingresoGenerado
        eventoMayor = i
        for j in range(len(eventos[i:])):
            if eventos[j+i].ingresoGenerado > mayor:
                mayor = eventos[j+i].ingresoGenerado
                eventoMayor = j+i
        
        aux = eventos[eventoMayor]
        eventos[eventoMayor] = eventos[i]
        eventos[i] = aux

    for i in range(len(comida)-1):
        mayor = comida[i].vendidos
        masVenta = i
        for j in range(len(comida[i:])):
            if comida[j+i].vendidos > mayor:
                mayor = comida[j+i].vendidos
                masVenta = j+i
        
        aux = comida[masVenta]
        comida[masVenta] = comida[i]
        comida[i] = aux

    print(f'--->Promedio de gasto de cliente:{promGasto//len(clientes)}$')
    print(f'--->% de clientes que no compran en feria:{(noFeria * 100)//len(clientes)}%')
    print('--->Clientes de mayor fidelidad:')
    for i in range(len(clientes)):
        print(f'{i+1}-', end='')
        clientes[i].informacion()
        print('')
        if i == 2:
            break
    print('--->Eventos con mayores ingresos:')
    for i in range(len(eventos)):
        if eventos[i].ingresoGenerado > 0: 
            print(f'{i+1}-{eventos[i].nombre}')
            print('Ingreso generado:', eventos[i].ingresoGenerado, '$\n')
        if i == 2:
            break
    print('--->Productos más vendidos en feria:')
    for i in range(len(comida)):
        if comida[i].vendidos > 0: 
            print(f'{i+1}-{comida[i].nombre}', end=': ')
            print(f'{comida[i].vendidos} unidades vendidas')
        if i == 4:
            break

    input('\nPresione ENTER para volver al menú principal')

from functions import *
from gestionComida import gestionComida
from gestionEventos import gestionEventos
from ventaTickets import ventaTickets
from ventaFeria import ventaFeria
from estadistica import estadistica

def main():

    seVendeTickets = True
    #obtener data proveniente de API
    data = init_data()
    #crear lista de eventos
    eventos = crearEventos(data["events"])
    #crear menú de feria
    comida = crearFeria(data['food_fair_inventory'])
    #crear clientes
    clientes = crearClientes()
    #ocupar asientos comprados
    eventos = ocuparAsientos(eventos, clientes)
    #Ajustar la cantidad de productos de comida
    comida = ajustarInventario(comida)

    while True:
        clear()
        print('******************************')
        print('          SAMANSHOW')
        print('******************************\n')

        print('¿Qué desea hacer?\n')
        print('===>Gestionar eventos (1)')
        print('===>Vender tickets (2)')
        print('===>Gestionar feria de comida (3)')
        print('===>Vender comida (4)')
        print('===>Estadísticas (5)')
        print('===>Salir (6)')
        opcion = input('===>Opción: ')

        #El programa entra en el módulo escogido
        if opcion == '1':
            seVendeTickets = gestionEventos(eventos, seVendeTickets)
            continue
        elif opcion == '2':
            clear()
            if seVendeTickets:
                clientes.append(ventaTickets(eventos))
                continue
            else:
                print('la venta de tickets está cerrada')
                input('Presione enter para volver al menú principal')
                continue
        elif opcion == '3':
            gestionComida(comida)
            continue
        elif opcion == '4':
            ventaFeria(comida, clientes)
            guardarCambios(clientes)
            continue
        elif opcion == '5':
            if len(clientes) > 0:
                estadistica(clientes, eventos, comida)
        else:
            clear()
            break
main()

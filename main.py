from functions import *
from gestionComida import gestionComida
from gestionEventos import gestionEventos
from ventaTickets import ventaTickets

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
        print('===>Salir (5)')
        opcion = input('===>Opción: ')

        if opcion == '1':
            seVendeTickets = gestionEventos(eventos, seVendeTickets)
            continue
        elif opcion == '2':
            clear()
            if seVendeTickets:
                ventaTickets(eventos)
                continue
            else:
                print('la venta de tickets está cerrada')
                input('Presione enter para volver al menú principal')
                continue
        elif opcion == '3':
            gestionComida(comida)
            continue
        elif opcion == 4:
            continue
        else:
            clear()
            break
main()
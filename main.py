from functions import *
from gestionComida import gestionComida
from gestionEventos import gestionEventos
from ventaTickets import ventaTickest

def main():

    venta_tickets = True
    #obtener data proveniente de API
    data = init_data()
    #crear lista de eventos
    eventos = crearEventos(data["events"])
    #crear menú de feria
    comida = crearFeria(data['food_fair_inventory'])

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
            venta_tickets = gestionEventos(eventos, venta_tickets)
            continue
        elif opcion == '2':
            if venta_tickets:
                venta_tickets(eventos)
                continue
            else:
                print('la venta de tickets está cerrada')
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
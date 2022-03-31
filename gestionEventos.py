from functions import crearMapa, clear


def gestionEventos(eventos, venta_tickets):
    while True:
        clear()
        print('******************************')
        print('      GESTIÓN DE EVENTOS')
        print('******************************\n')

        print('¿Qué desea hacer?\n')
        print('===>Ver eventos (1)')
        print('===>Buscar eventos (2)')
        if venta_tickets:
            print('===>Cerrar venta de tickets (3)')
        else:
            print('===>Abrir venta de tickets (3)')
        print('===>Menú principal (4)')
        opcion = input('===>Opción: ')

        clear()

        if opcion == '1':
            #muesta información de todos los eventos
            for evento in eventos:
                print('----------------------------------------------')
                evento.info()
                print('Asientos:')
                crearMapa(evento.mapa, evento.sillasOcupadas)
        elif opcion == '2':
            #busca eventos mediante filtros
            print('¿Qué filtro desea aplicar?\n')
            print('===>Tipo (1)')
            print('===>Fecha (2)')
            print('===>Actor o cantante (3)')
            print('===>Nombre de evento (4)')
        
            opcion = input('===>Opción: ')
            
            clear()

            if opcion == '1':
                tipo = input('\n===>Ingrese tipo de evento (Musical) (Teatro): ').capitalize()
                if tipo == 'Musical' or tipo == 'Teatro':
                    for evento in eventos:
                        if evento.tipo == tipo:
                            print('----------------------------------------------')
                            evento.info()
                            print('Asientos:')
                            crearMapa(evento.mapa, evento.sillasOcupadas)
            elif opcion == '2':
                year = input('\nAño: ')
                mes = input('Mes: ')
                dia = input('Día: ')

                fecha = f'{year}-{mes}-{dia}'
                for evento in eventos:
                        if evento.fecha == fecha:
                            print('----------------------------------------------')
                            evento.info()
                            print('Asientos:')
                            crearMapa(evento.mapa, evento.sillasOcupadas)
            elif opcion == '3':
                persona = input('\nIngrese nombre de actor/cantante: ')
                for evento in eventos:
                        if persona in evento.cartel:
                            print('----------------------------------------------')
                            evento.info()
                            print('Asientos:')
                            crearMapa(evento.mapa, evento.sillasOcupadas)
            elif opcion == '4':
                nombre = input('\nIngrese nombre de evento: ')
                for evento in eventos:
                        if evento.nombre == nombre:
                            print('----------------------------------------------')
                            evento.info()
                            print('Asientos:')
                            crearMapa(evento.mapa, evento.sillasOcupadas)
                            break
        elif opcion == '3':
            #cierra o abre la venta de tickets, al iniciar siempre estará abierta hasta usar esta opción
            venta_tickets = not venta_tickets
            if venta_tickets:
                print('Venta de tickets abierta')
            else:
                print('Venta de tickets cerrada')
        else:
            break
        
        continuar = input('\n\n===>Gestionar eventos (1)\n===>Menú principal (2)\n===>Opción: ')
        if continuar == '1':
            clear()
            continue
        else:
            clear()
            break

    return venta_tickets
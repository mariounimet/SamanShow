from operator import indexOf
from functions import crearMapa


def gestionEventos(eventos):
    print('******************************')
    print('      GESTIÓN DE EVENTOS')
    print('******************************\n')

    print('¿Qué desea hacer?\n')
    print('===>Ver eventos (1)')
    print('===>Buscar eventos (2)')
    print('===> (3)')
    opcion = input('===>Opción: ')

    if opcion == '1':
        for evento in eventos:
            print('----------------------------------------------')
            evento.info()
            print('Asientos:')
            crearMapa(evento.mapa, evento.sillasOcupadas)
    elif opcion == '2':
        print('¿Qué filtro desea aplicar?\n')
        print('===>Tipo (1)')
        print('===>Fecha (2)')
        print('===>Actor o cantante (3)')
        print('===>Nombre de evento (4)')
        opcion = input('===>Opción: ')

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
        else:
            print('Tipo de evento no válido')


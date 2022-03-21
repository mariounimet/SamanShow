from functions import *
from gestionEventos import gestionEventos

def main():

    #obtener data proveniente de API
    data = init_data()
    eventos = crearEventos(data["events"])

    print('******************************')
    print('          SAMANSHOW')
    print('******************************\n')

    print('¿Qué desea hacer?\n')
    print('===>Gestionar eventos (1)')
    print('===>Vender tickets (2)')
    print('===>Gestionar feria de comida (3)')
    print('===>Vender comida (4)')
    opcion = input('===>Opción: ')

    if opcion == '1':
        gestionEventos(eventos)


main()
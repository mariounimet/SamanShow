import requests
from EventoMusical import *
from EventoTeatro import *

def init_data():
    print('cargando datos...')
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print('datos cargados')
        return data

def crearEventos(data):
    print("cargando eventos")
    lista = []
    for evento in data:
        if evento['type'] == 1:
            nombre = evento['title']
            bandas = evento['bands']
            cartel = evento['cartel']
            fecha = evento['date']
            precios = {'g': evento['prices'][0], 'v': evento['prices'][1]}
            mapa = []

            for i in range(evento['layout']['vip'][0]):
                for j in range(evento['layout']['vip'][1]):
                    mapa.append(f'V{i+1}-{j+1}')
                mapa.append('-')
            for i in range(evento['layout']['general'][0]):
                for j in range(evento['layout']['general'][1]):
                    mapa.append(f'G{i+1}-{j+1}')
                mapa.append('-')
            
            
            lista.append(EventoMusical(nombre, 'Musical', cartel, mapa, precios, fecha, bandas))

        if evento['type'] == 2:
            nombre = evento['title']
            sinopsis = evento['synopsis']
            cartel = evento['cartel']
            fecha = evento['date']
            precios = {'g': evento['prices'][0], 'v': evento['prices'][1]}
            mapa = []

            for i in range(evento['layout']['vip'][0]):
                for j in range(evento['layout']['vip'][1]):
                    mapa.append(f'V{i+1}-{j+1}')
                mapa.append('-')
            for i in range(evento['layout']['general'][0]):
                for j in range(evento['layout']['general'][1]):
                    mapa.append(f'G{i+1}-{j+1}')
                mapa.append('-')
            
            lista.append(EventoTeatro(nombre, 'Teatro', cartel, mapa, precios, fecha, sinopsis))
    print('eventos cargados\n')
    return lista

def crearMapa(lista, ocupados):
    
    print('      ----------------------------------------------')
    print('                         ESCENARIO')
    print('      ----------------------------------------------')
    for i in lista:
        if i not in ocupados and i != '-':
            print(i, end='|-|')
        elif i not in ocupados:
            print('\n')
        else:
            print('xxxx', end='')
        
    print('')
    
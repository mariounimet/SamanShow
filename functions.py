import requests
import os
from Cliente import Cliente
from Evento import EventoMusical, EventoTeatro
from Comida import Alimento, Bebida

def init_data():
    print('cargando datos...')
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print('datos cargados')
        return data

def clear():  #codigo de función obtenido de: https://micro.recursospython.com/recursos/como-limpiar-la-consola.html
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def crearEventos(data):
    print("cargando eventos...")
    lista = []
    for evento in data:

        nombre = evento['title']
        cartel = evento['cartel']
        fecha = evento['date']
        precios = {'G': evento['prices'][0], 'V': evento['prices'][1]}
        mapa = []

        for i in range(evento['layout']['vip'][0]):
            for j in range(evento['layout']['vip'][1]):
                mapa.append(f'V{i+1}-{j+1}')
            mapa.append('-')
        for i in range(evento['layout']['general'][0]):
            for j in range(evento['layout']['general'][1]):
                mapa.append(f'G{i+1}-{j+1}')
            mapa.append('-')

        if evento['type'] == 1:
            bandas = evento['bands']
            
            lista.append(EventoMusical(nombre, 'Musical', cartel, mapa, precios, fecha, bandas))

        elif evento['type'] == 2:
            sinopsis = evento['synopsis']

            lista.append(EventoTeatro(nombre, 'Teatro', cartel, mapa, precios, fecha, sinopsis))
    print('eventos cargados')
    return lista


def crearFeria(data):
    print("cargando feria...")
    lista = []
    for producto in data:
        nombre = producto['name']
        precio = producto['price']
        cantidad = producto['amount']

        if producto['type'] == 1:
            if producto['presentation'] == 1:
                presentacion = 'Preparación'
            else:
                presentacion = 'Empaque'
            lista.append(Alimento(nombre, 'Alimento', precio, cantidad, presentacion))
        elif producto['type'] == 2:
            lista.append(Bebida(f'{nombre} pequeño', 'Bebida', precio[0], cantidad//3, 'pequeño'))
            lista.append(Bebida(f'{nombre} mediano', 'Bebida', precio[1], cantidad//3, 'mediano'))
            lista.append(Bebida(f'{nombre} grande', 'Bebida', precio[2], cantidad//3, 'grande'))
    print('feria cargada')
    return lista

def crearClientes():
    file = open('clientes.txt', 'r')

    clientes = []

    aux = 0
    nombre = ''
    ci = ''
    edad = ''
    eventoNombre = ''
    montoEvento = 0
    montoFeria = 0
    asientos = []
    comida = []
    for fila in file:
        if aux == 0:
            datos = fila.split('|')
            nombre = datos[0]
            ci = datos[1]
            edad = datos[2]
            eventoNombre = datos[3]
            montoEvento = datos[4]
            montoFeria = datos[5]
            aux += 1
            continue
        elif aux == 1:
            asientos = fila.split('|')
            asientos.pop(-1)
            aux += 1
            continue
        elif aux == 2:
            if fila != '-':
                comida = fila.split('|')
                comida.pop(-1)
            clientes.append(Cliente(nombre, ci, edad, eventoNombre, asientos, montoEvento, montoFeria, comida))
            aux = 0
            continue
    file.close()
    return clientes
    
def ocuparAsientos(eventos, clientes):
    
    for cliente in clientes:
        for evento in eventos:
            if cliente.evento == evento.nombre:
                evento.sillasOcupadas.extend(cliente.asientos)
                break
    return eventos

def ajustarInventario(comida, clientes):
    for cliente in clientes:
        for producto in comida:
            if producto.nombre in cliente.comida:
                i = cliente.comida.count(producto.nombre)
                producto.vender(i)

    return comida

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
            print('xxxx', end='|-|')
        
    print('')
    
def vampiro(num):
    if len(num) % 2 != 0:
        return False
    

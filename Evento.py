from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nombre, tipo, cartel, mapa, precios, fecha):

        self.nombre = nombre
        self.tipo = tipo
        self.cartel = cartel
        self.mapa = mapa
        self.precios = precios
        self.fecha = fecha
        self.sillasOcupadas = []
        self.ingresoGenerado = 0

    @abstractmethod
    def info(self):
        pass

class EventoMusical(Evento):
    def __init__(self, nombre, tipo, cartel, mapa, precios, fecha, bandas):
        Evento.__init__(self, nombre, tipo, cartel, mapa, precios, fecha)

        self.bandas = bandas

    def info(self):
        print(f'Nombre: {self.nombre}',
        f'\nTipo: {self.tipo}',
        f'\nBandas: {self.bandas}',
        f'\nCartel: {self.cartel}',
        f'\nPrecios: {self.precios}',
        f'\nFecha: {self.fecha}')
        print('')

class EventoTeatro(Evento):
    def __init__(self, nombre, tipo, cartel, mapa, precios, fecha, sinopsis):
        Evento.__init__(self, nombre, tipo, cartel, mapa, precios, fecha)

        self.sinopsis = sinopsis

    def info(self):
        print(f'Nombre: {self.nombre}',
        f'\nSinopsis: {self.sinopsis}'
        f'\nTipo: {self.tipo}',
        f'\nCartel: {self.cartel}',
        f'\nPrecios: {self.precios}',
        f'\nFecha: {self.fecha}')
        print('')
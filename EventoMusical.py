from Evento import Evento

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
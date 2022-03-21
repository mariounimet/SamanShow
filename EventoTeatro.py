from Evento import Evento

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
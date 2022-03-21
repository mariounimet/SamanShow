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

    @abstractmethod
    def info(self):
        pass


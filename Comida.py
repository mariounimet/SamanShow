from abc import ABC, abstractmethod

class Comida(ABC):
    def __init__(self, nombre, clasificacion, precio, cantidad):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.precio = round(precio + (precio * 0.16), 2)
        self.cantidad = cantidad
        self.vendidos = 0

    @abstractmethod
    def info(self):
        pass

    def vender(self, veces):
        for i in range(veces):
            self.cantidad -= 1
            self.vendidos += 1

class Bebida(Comida):
    def __init__(self, nombre, clasificacion, precio, cantidad, tamano):
        super().__init__(nombre, clasificacion, precio, cantidad)

        self.tamano = tamano

    def info(self):
        print(f'\n*{self.nombre}')
        print(f'-Precio: {self.precio}')
        print(f'-Existencia: {self.cantidad}')

class Alimento(Comida):
    def __init__(self, nombre, clasificacion, precio, cantidad, presentacion):
        super().__init__(nombre, clasificacion, precio, cantidad)
        
        self.presentacion = presentacion

    def info(self):
        print(f'\n*{self.nombre}')
        print(f'-Presentación: {self.presentacion}')
        print(f'-Precio: {self.precio}')
        print(f'-Existencia: {self.cantidad}')
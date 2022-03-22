from abc import ABC, abstractmethod

class Comida(ABC):
    def __init__(self, nombre, clasificacion, precio, cantidad):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.precio = round(precio + (precio * 0.16), 2)
        self.cantidad = cantidad

    @abstractmethod
    def info(self):
        pass

class Bebida(Comida):
    def __init__(self, nombre, clasificacion, precio, cantidad, tamano):
        super().__init__(nombre, clasificacion, precio, cantidad)

        self.tamano = tamano

    def info(self):
        print(f'\n*{self.nombre}')
        print(f'-Tamaño: {self.tamano},')
        print(f'-Precio: {self.precio}')
        print(f'-Existencia: {self.cantidad}')

class Alimento(Comida):
    def __init__(self, nombre, clasificacion, precio, cantidad, presentacion):
        super().__init__(nombre, clasificacion, precio, cantidad)
        
        self.presentacion = presentacion

    def info(self):
        pass
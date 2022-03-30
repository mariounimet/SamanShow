from Comida import Comida


class Cliente:
    def __init__(self, nombre, ci, edad, evento, asientos, montoEvento, montoFeria=0, comida=[]):
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.evento = evento
        self.asientos = asientos
        self.montoEvento = float(montoEvento)
        self.montoFeria = float(montoFeria)
        self.comida = comida

    def totalMonto(self):
        return self.montoEvento + self.montoFeria

    def informacion(self):
        print(self.nombre)
        print('CI: ', self.ci)
        print('Edad: ', self.edad)
        print('Evento: ', self.evento)
        print('Asientos: ')
        for i in self.asientos:
            print('-', i)
        print(self.comida)
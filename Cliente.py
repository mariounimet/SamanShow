from Comida import Comida


class Cliente:
    def __init__(self, nombre, ci, edad, evento, asientos, montoEvento, montoFeria=0):
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.evento = evento
        self.asientos = asientos
        self.montoEvento = round(float(montoEvento), 2)
        self.montoFeria = round(float(montoFeria), 2)

    def totalMonto(self):
        return self.montoEvento + self.montoFeria

    def informacion(self):
        print(self.nombre)
        print('CI: ', self.ci)
        print('Edad: ', self.edad)
        print('Evento: ', self.evento)
        print(f'Total pagado: {self.totalMonto()}')
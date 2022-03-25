class Cliente:
    def __init__(self, nombre, ci, edad, evento, asientos, montoEvento):
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.evento = evento
        self.asientos = asientos
        self.montoEvento = montoEvento
        self.montoFeria = 0

        self.comida = []

    def totalMonto(self):
        return self.montoEvento + self.montoFeria
class Event:
    def __init__(self, name, type, cartel, layout, prices, date):

        self.name = name
        self.type = type
        self.cartel = cartel
        self.layout = layout
        self.prices = prices
        self.date = date

class MusicalEvent(Event):
    def __init__(self, name, type, cartel, layout, prices, date, bands):
        Event.__init__(self, name, type, cartel, layout, prices, date)

        self.bands = bands

    def show(self):
        print(f'Name: {self.name}',
        f'\nType: {self.type}',
        f'\nBands: {self.bands}',
        f'\nCartel: {self.cartel}',
        f'\nLayout: {self.layout}',
        f'\nPrices: {self.prices}',
        f'\nDate: {self.date}')

class TeatherEvent(Event):
    def __init__(self, name, type, cartel, layout, prices, date, synopsis):
        Event.__init__(self, name, type, cartel, layout, prices, date)

        self.synopsis = synopsis

    def show(self):
        print(f'Name: {self.name}',
        f'\nSynopsis: {self.synopsis}'
        f'\nType: {self.type}',
        f'\nCartel: {self.cartel}',
        f'\nLayout: {self.layout}',
        f'\nPrices: {self.prices}',
        f'\nDate: {self.date}')
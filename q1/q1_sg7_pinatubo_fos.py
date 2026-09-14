class Glassware:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Glassware: {self.name}")


class Beaker(Glassware):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def display(self):
        print(f"Beaker: {self.name}, Capacity: {self.capacity} mL")


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Beaker 1", 100),
            Beaker("Beaker 2", 250),
            Beaker("Beaker 3", 500),
            Beaker("Beaker 4", 1000),
            Beaker("Beaker 5", 2000)
        ]

    def display(self):
        print("Tray contains:")
        for beaker in self.beakers:
            beaker.display()

tray = Tray()
tray.display()

del tray
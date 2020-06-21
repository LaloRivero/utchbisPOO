class Vehiculos:
    def __init__(self):
        pass

    def avanza(self):
        print('Avanza')


class Automoviles(Vehiculos):
    def __init__(self):
        super().__init__()

    def avanza(self):
        print('Soy un automovil y avanzo en 4 ruedas')


class Avion(Vehiculos):
    def __init__(self):
        super().__init__()

    def avanza(self):
        print('Soy un avion y vuelo por el aire')


class Lancha(Vehiculos):
    def __init__(self):
        super().__init__()

    def avanza(self):
        print('Soy una lancha y navego por el agua')


if __name__ == "__main__":
    carro = Automoviles()
    avion = Avion()
    lancha = Lancha()
    carro.avanza()
    avion.avanza()
    lancha.avanza()

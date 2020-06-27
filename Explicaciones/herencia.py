class Cuadrilatero:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura


class Rectangulo(Cuadrilatero):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def type_rectangulo(self):
        print('Soy un rectangulo')


class Cuadrado(Cuadrilatero):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def type_cuadrado(self):
        print('Soy un Cuadrado')


if __name__ == "__main__":
    cuadrado = Cuadrado(5)
    rectangulo = Rectangulo(15, 10)

    area_c = cuadrado.calc_area()
    cuadrado.type_cuadrado()
    print(f'Mi area es: {area_c} \n')

    area_r = rectangulo.calc_area()
    rectangulo.type_rectangulo()
    print(f'Mi area es: {area_r}')

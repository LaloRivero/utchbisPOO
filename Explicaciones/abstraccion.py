class Lavadora:
    def __init__(self):
        pass

    def lavar(self):
        self._llenar_el_tanque_de_agua()
        self._agregar_detergente()
        self._lavar()
        self._enjuagar()
        self._drenar_agua()
        self._secado()

    def _llenar_el_tanque_de_agua(self):
        print('Llenando el tanque de agua')

    def _agregar_detergente(self):
        print('Agregando detergente')

    def _lavar(self):
        print('Lavando')

    def _enjuagar(self):
        print('Enjuagando')

    def _drenar_agua(self):
        print('Drenando el agua')

    def _secado(self):
        print('Secando la ropa')


if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()

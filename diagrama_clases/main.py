# - Computadora -> Laptop -> PC de escritorio -> all-in-one -> servidor
# - Automovil -> sedan -> hastback -> pick-up -> SUVs -> Tipo van
# - Celular -> SmartPhone (IOS, Android, Huawei, WindowPhone) -> notSmartPhone
# - Pluma -> Gel -> PlumaFuente -> PlumaBorrable -> PlumaInvisible
# - Guitarra -> Acustica -> Electrica -> Electroacustica -> Guitarron -> BajoSexto -> Requinto

class Computadora:
    def __init__(self,brand, model, screen, cpu, ram, HDD=500):
        self.brand = brand
        self.model = model
        self.screen = screen
        self.cpu = cpu
        self.ram = ram
        self.HDD = HDD
    
    def turn_on(self):
        print('Turning on')
    
    def open_apps(self):
        print('Open Apps')
        
    def turn_off(self):
        print('Turning off')
        


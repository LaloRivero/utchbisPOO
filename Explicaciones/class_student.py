class student():

    def __init__(self, name=str, age=int, group=str, id_s=int, career=str):
        self.name = name
        self.age = age
        self.group = group
        self.id_s = id_s
        self.career = career

    def saludar(self):
        print(f'Hola mi nombre es {self.name}')

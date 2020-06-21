utchbis21 = {
    '1113120063': 'ENRIQUEZ MARQUEZ ISAAC ALBERTO',
    '1118170013': 'OLIVA PRIETO MIGUEL HABACUC',
    '1119220016': 'CANALES FUENTES JESUS GIBRAN',
    '6519150003': 'GAMBOA HEREDIA MIGUEL ANGEL',
    '6519150005': 'DAVILA GOVEA ANGEL ARTURO',
    '6519150006': 'BRAVO RODRIGUEZ SAUL URIEL',
    '6519150007': 'ROJAS GALLARDO GABRIELA',
    '1119150014': 'GARCIA MOLINA OBED RAUL',
    '6519150009': 'DECANINI SORIANO BRAYAN ALEJANDRO',
    '6519150011': 'OROZCO PEREZ CARLOS ADRIAN',
    '6519150014': 'LOPEZ OROZCO JESUS ALBERTO',
    '6519140001': 'RIVAS TREJO EDGAR ALEJANDRO',
    '6519150021': 'FIERRO GALVAN ULISES',
    '6519150027': 'CARBALLO MACIAS ANGEL',
    '6519150028': 'RUIZ CHUMACERO DAVID ALBERTO',
    '6519150032': 'PRIETO LOZOYA BRAYAN',
    '6519150033': 'LOPEZ PIÑON HORACIO EMILIO',
    '6519150034': 'RICO GRANADOS JONATAN CALEB',
    '6519150038': 'MOLINA REZA PRISCILA FERNANDA',
}
utchbis22 = {
    '6518150041': 'TREJO ARMENTA DAVID',
    '6519150001': 'SOSA REYES MICHELL',
    '6519150002': 'CHACON DIAZ MAURICIO EDUARDO',
    '6519150004': 'TARANGO DE LA VEGA FERNANDO',
    '6519150012': 'ERIVES CHAVEZ CESAR',
    '6519150013': 'ARIZMENDI ROMERO ANGEL SAUL',
    '6519150015': 'RAMOS DELGADO DIANA',
    '6519150016': 'MEDIANO ARAMBULA MARCOS',
    '6519150017': 'GONZALEZ CHAVIRA ANA SOFIA',
    '6519150019': 'ACOSTA DOMINGUEZ CARLOS RODRIGO',
    '6519150022': 'TORRES BORUNDA ILSE PAULINA',
    '6519150025': 'RAMOS CASTRO RENE ALEJANDRO',
    '6519150026': 'RUIZ ROMERO MAURICIO EMANUEL',
    '6519150029': 'MURILLO CRUZ MARIBEL',
    '6519150031': 'SIGALA FERNANDEZ LUIS CARLOS',
    '6519150035': 'PEREZ LOPEZ CARLOS EDUARDO',
    '6519150036': 'TORRALBA RUIZ CANEK ELEAZAR',
    '6519150037': 'VELARDE MUÑOZ MIGUEL ANGEL',
    '6519140002': 'BARRAGAN AGUILAR ESTEFANIA',
}

students = []

# Cambiar el nombre a Nombre Apellido


class Student:
    def __init__(self, name, last_name, group, matricula):
        self.name = name
        self.last_name = last_name
        self.group = group
        self.matricula = matricula

    def show_first_name(self):
        return self.name

    def show_last_name(self):
        return self.last_name

    def show_len_of_full_name(self):
        return len(self.name+self.last_name)


def show_students_with_():
    # show students that last name starts with R
    for student in students:
        if student.last_name.startswith('R'):
            print(f'{student.name} {student.last_name}')


def show_21m_students():
    for student in students:
        if student.group == 'utchbis21':
            print(f'{student.name} {student.last_name}')


def show_22m_students():
    for student in students:
        if student.group == 'utchbis21':
            print(f'{student.name} {student.last_name}')


def create_students():

    for key, values in utchbis21.items():
        full_name = values.split()

        if len(full_name) >= 4:
            name = full_name[2] + ' ' + full_name[3]
        else:
            name = full_name[2]

        last_name = ''.join(full_name[0] + ' ' + full_name[1])

        students.append(Student(name, last_name, group='utchbis21', matricula=key))

    for key, values in utchbis22.items():
        full_name = values.split()

        if len(full_name) >= 4:
            name = full_name[2] + ' ' + full_name[3]
        else:
            name = full_name[2]

        last_name = ''.join(full_name[0] + ' ' + full_name[1])

        students.append(Student(name, last_name, group='utchbis21', matricula=key))


def main():
    create_students()
    print('Students with R')
    show_students_with_()
    print('Group 21m')
    show_21m_students()


if __name__ == "__main__":
    main()

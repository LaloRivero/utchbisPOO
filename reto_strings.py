import sys


utchbis21 = {
    '1113120063': 'ENRIQUEZ MARQUEZ ISAAC ALBERTO',
    '1118170013': 'OLIVAS PRIETO MIGUEL HABACUC',
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
    '6519150031': 'SIGALA FERNANDEZ	LUIS CARLOS',
    '6519150035': 'PEREZ LOPEZ CARLOS EDUARDO',
    '6519150036': 'TORRALBA RUIZ CANEK ELEAZAR',
    '6519150037': 'VELARDE MUÑOZ MIGUEL ANGEL',
    '6519140002': 'BARRAGAN AGUILAR	ESTEFANIA',
}

# Cambiar el nombre a Nombre Apellido


class Student:
    def __init__(self, name, last_name, group, id):
        self.name = name
        self.last_name = last_name
        self.group = group
        self.id = id

    def show_first_name(self):
        print(self.name)

    def show_last_name(self):
        print(self.last_name)

    def show_len_of_full_name(self):
        print(len(self.name + self.last_name))


def show_students_with_(students):
    # show students that last name starts with R
    for student in students:
        if student.last_name.startswith('R'):
            print(f'{student.name} {student.last_name}')


def show_21m_students(students):
    for student in students:
        if student.group == "utchbis21m":
            print(f'{student.name} {student.last_name}')


def show_22m_students(students):
    for student in students:
        if student.group == "utchbis22m":
            print(f'{student.name} {student.last_name}')


def create_students():
    students = []

    for key, values in utchbis21.items():
        full_name = values.split()
        if len(full_name) < 4:
            first_name = full_name[2]
        else:
            first_name = full_name[2] + ' ' + full_name[3]
        last_name = full_name[0] + ' ' + full_name[1]
        students.append(Student(first_name, last_name, group='utchbis21m', id=key))
    for key, values in utchbis22.items():
        full_name = values.split()
        if len(full_name) < 4:
            first_name = full_name[2]
        else:
            first_name = full_name[2] + ' ' + full_name[3]
        last_name = full_name[0] + ' ' + full_name[1]
        students.append(Student(first_name, last_name, group='utchbis22m', id=key))

    return students


def create_new_student(students):
    msj = 'Adding new students:'
    print(msj.center(50, '-'))

    while True:
        last_name = input('Type your last name: ').upper()
        if len(last_name) < 3:
            print('ERROR last name not valid, please try again.')
        elif last_name == 'EXIT':
            sys.exit()
        else:
            break

    while True:
        first_name = input('Type your name: ').upper()
        if len(first_name) < 3:
            print('ERROR name not valid, please try again.')
        elif first_name == 'EXIT':
            sys.exit()

        else:
            break

    while True:
        group = input('''

                    [1] utch-bis-21m
                    [2] utch-bis-22m

                    ''')
        if group == '1':
            group = 'utchbis21m'
            break
        elif group == '2':
            group = 'utchbis22m'
            break
        elif group == 'exit':
            sys.exit()
        else:
            print('ERROR group not valid, please try again.')

    while True:
        id = input('Type your id: ')

        if id == 'exit':
            sys.exit()
        elif len(id) != 10:
            print('ERROR id not valid, please try again.')
        else:
            break

    students.append(Student(first_name, last_name, group, id))


def show_all_students(students):
    for student in students:
        print(f'{student.name} {student.last_name}')


def show_student_by_id(students):

    while True:
        student_id = input('Type student id: ')
        if student_id == 'exit':
            sys.exit()
        elif len(student_id) != 10:
            print('ERROR id not valid, please try again.')
        else:
            break

    flag = False
    for student in students:
        if student_id == student.id:
            print(f'The student with id number: {student.id} is {student.name} {student.last_name}')
            flag = True
            break

    if flag == False:
        print('ERROR student not found')


def main():
    students = create_students()
    groups = ['utchbis21m', 'utchbis22m']
    while True:
        op = input('''

            [1] Add new student
            [2] View all students
            [3] Show groups
            [4] Search student by id
            [5] Show students by group
            [6] Exit

            ''')

        if op == '1':
            create_new_student(students)
        elif op == '2':
            show_all_students(students)
        elif op == '3':
            for group in groups:
                print(group)
        elif op == '4':
            show_student_by_id(students)
        elif op == '5':
            group = input('''
                        [1] UTCH-BIS21m
                        [2] UTCH-BIS22m
                        ''')
            if group == '1':
                show_21m_students(students)
            elif group == '2':
                show_22m_students(students)
        else:
            break


if __name__ == "__main__":
    main()

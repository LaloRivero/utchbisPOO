import sys
import csv

from class_student import Student
from validation import validate_data
# Cambiar el nombre a Nombre Apellido

STUDENT_TABLE = 'students.csv'
STUDENTS_SCHEMA = ['last_name', 'name', 'group', 'id']
students = []


def _initialize_students_from_storage():
    with open(STUDENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=STUDENTS_SCHEMA)
        for row in reader:
            students.append(row)


def create_student():
    msj = ' Creating new student '
    print(msj.center(50, '-'))

    last_name = validate_data('last_name')
    first_name = validate_data('first_name')
    group = validate_data('group')
    student_id = validate_data('student_id')
    student = Student(first_name, last_name, group, student_id)

    with open(STUDENT_TABLE, mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=STUDENTS_SCHEMA)
        writer.writerow(student.to_dict())


def show_students_by_group(group):
    msj = f' Group {group} '
    print(msj.center(50, '-'))

    for student in students:
        if student['group'] == group:
            print(f"{student['id']} | {student['name']} {student['last_name']}  ")


def main():
    _initialize_students_from_storage()
    groups = ['utchbis21m', 'utchbis22m']

    op = input('''

        [C] Create student
        [R] Search student by id
        [U] Update student data by id
        [D] Delete student by id
        [S] Show students by group
        [E] Exit

        ''')
    op = op.upper()
    if op == 'C':
        create_student()
    elif op == '2':
        pass  # show_all_students()
    elif op == '3':
        for group in groups:
            print(group)
    elif op == '4':
        pass  # show_student_by_id()
    elif op == 'S':
        group = input('''
        [1] utchbis21m
        [2] utchbis22m
        ''')
        if group == '1':
            show_students_by_group('utchbis21')
        else:
            show_students_by_group('utchbis22')
    else:
        sys.exit()


if __name__ == "__main__":
    main()
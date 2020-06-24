import sys
import csv
import os

from class_student import Student
from validation import validate_data
from update_data import update_data
# Cambiar el nombre a Nombre Apellido

STUDENT_TABLE = 'students.csv'
STUDENTS_SCHEMA = ['last_name', 'name', 'group', 'id']
students = []


def _initialize_students_from_storage():
    with open(STUDENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=STUDENTS_SCHEMA)
        for row in reader:
            students.append(row)


def _save_students_to_storage():
    tmp_table_name = f'{STUDENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=STUDENTS_SCHEMA)
        writer.writerows(students)
        f.close()
        os.remove(STUDENT_TABLE)
        os.rename(tmp_table_name, STUDENT_TABLE)


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


def search_student_by_id(_id):
    msj = f' Search Student '
    print(msj.center(50, '-'))

    for student in students:
        if student['id'] == _id:
            print(f"{student['id']} | {student['name']} {student['last_name']} | {student['group']}")


def update_student_data_by_id(_id):
    msj = f' Update Student Data'
    print(msj.center(50, '-'))

    for student in students:
        if student['id'] == _id:
            student = update_data(student)

    _save_students_to_storage()


def delete_student_by_id(_id):
    msj = f' Delete Student '
    print(msj.center(50, '-'))

    for i, student in enumerate(students):
        if student['id'] == _id:
            print(f"{student['id']} | {student['name']} {student['last_name']} | {student['group']}")
            sure = input('Are you sure to delete this student?[Y/Enter to exit]')
            if sure == 'Y':
                del students[i]
            else:
                sys.exit()
    _save_students_to_storage()


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
    elif op == 'R':
        _id = validate_data('student_id')
        search_student_by_id(_id)
    elif op == 'U':
        _id = validate_data('student_id')
        update_student_data_by_id(_id)
    elif op == 'D':
        _id = validate_data('student_id')
        delete_student_by_id(_id)
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

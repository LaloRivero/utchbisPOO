import sys
import csv
import os

from Student import Student
from validation import validate_data

STUDENTS_TABLE = 'students.csv'
STUDENTS_SCHEMA = ['last_name', 'name', 'group', 'id']
students = []


def _initialize_students_from_storage():
    with open(STUDENTS_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=STUDENTS_SCHEMA)
        for row in reader:
            students.append(row)


def create_student():
    global students
    msj = 'Creating new student'
    print(msj.center(50, '-'))

    last_name = validate_data('last_name')
    first_name = validate_data('first_name')
    group = validate_data('group')
    student_id = validate_data('student_id')
    student = Student(first_name, last_name, group, student_id)

    with open(STUDENTS_TABLE, mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=STUDENTS_SCHEMA)
        writer.writerow(student.to_dict())


def search_student_by_id(_id):
    msj = f' Student '
    print(msj.center(50, '-'))
    for student in students:
        if student['id'] == _id:
            print(f"{student['id']} | {student['name']} {student['last_name']}  ")
            break


def update_student_data_by_id(_id):
    msj = f' Update Data '
    print(msj.center(50, '-'))
    for student in students:
        if student['id'] == _id:
            update_data(student)

    tmp_table_name = '{}.tmp'.format(STUDENTS_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=STUDENTS_SCHEMA)
        writer.writerows(students)
        f.close()
        os.remove(STUDENTS_TABLE)
        os.rename(tmp_table_name, STUDENTS_TABLE)


def update_data(student):
    update_last_name = input("Update last name? [Y/N]")
    if update_last_name == 'Y':
        last_name = validate_data('last_name')
        student['last_name'] = last_name
    update_name = input("Update first name? [Y/N]")
    if update_name == 'Y':
        first_name = validate_data('first_name')
        student['name'] = first_name
    update_group = input("Update group? [Y/N]")
    if update_group == 'Y':
        group = validate_data('group')
        student['group'] = group
    update_student_id = input("Update student id? [Y/N]")
    if update_student_id == 'Y':
        student_id = validate_data('student_id')
        student['id'] = student_id
    msj = f' Updated Data '
    print(msj.center(50, '-'))
    print(f"{student['id']} | {student['name']} {student['last_name']} | {student['group']}")


def delete_student_by_id(_id):
    msj = f' Deleted Student '
    print(msj.center(50, '-'))
    flag = False
    for i, student in enumerate(students):
        if student['id'] == _id:
            print(f"{student['id']} | {student['name']} {student['last_name']} | {student['group']}")
            del students[i]
            flag = True

            tmp_table_name = '{}.tmp'.format(STUDENTS_TABLE)
            with open(tmp_table_name, mode='w') as f:
                writer = csv.DictWriter(f, fieldnames=STUDENTS_SCHEMA)
                writer.writerows(students)
                f.close()
                os.remove(STUDENTS_TABLE)
                os.rename(tmp_table_name, STUDENTS_TABLE)

    if flag == False:
        print('Student is not in student list')


def show_students_by_group(group):
    msj = f'Group {group}'
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

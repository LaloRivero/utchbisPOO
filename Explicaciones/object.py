from class_student import student


def main():
    student1 = student('David Ruiz', 19, 'utchBIS-21m', 6519150028, 'TI')
    student2 = student('Gabriela Rojas', 19, 'utchBIS-21m', 6519150007, 'TI')
    student3 = student('Priscila Molina', 20, 'utchBIS-21m', 6519150038, 'TI')

    student1.saludar()
    student2.saludar()
    student3.saludar()


if __name__ == "__main__":
    main()

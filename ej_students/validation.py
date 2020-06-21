def validate_data(type_of_data):
    import sys

    if type_of_data == 'last_name':
        while True:
            last_name = input('Type your last name: ').upper()
            if len(last_name) < 3:
                print('ERROR last name not valid, please try again.')
            elif last_name == 'EXIT':
                sys.exit()
            else:
                return last_name

    elif type_of_data == 'first_name':
        while True:
            first_name = input('Type your name: ').upper()
            if len(first_name) < 3:
                print('ERROR name not valid, please try again.')
            elif first_name == 'EXIT':
                sys.exit()
            else:
                return first_name

    elif type_of_data == 'group':
        while True:
            print('Select the group')
            group = input('''
            [1] utch-bis-21m
            [2] utch-bis-22m
                    ''')
            if group == '1':
                return 'utchbis21'
            elif group == '2':
                return 'utchbis22'
            elif group == 'exit':
                sys.exit()
            else:
                print('ERROR group not valid, please try again.')

    elif type_of_data == 'student_id':
        while True:
            student_id = input('Type your id: ')

            if student_id == 'exit':
                sys.exit()
            elif len(student_id) != 10:
                print('ERROR id not valid, please try again.')
            else:
                return student_id

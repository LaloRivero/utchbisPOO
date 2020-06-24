from validation import validate_data


def update_data(student):
    msj = f' Update Data '
    print(msj.center(50, '-'))

    # last_name
    update_last_name = input('Update last name? [Y/Enter to continue]')
    if update_last_name == 'Y':
        last_name = validate_data('last_name')
        student['last_name'] = last_name

    # first_name
    update_first_name = input('Update first name? [Y/Enter to continue]')
    if update_first_name == 'Y':
        first_name = validate_data('first_name')
        student['name'] = first_name
    # group

    update_group = input('Update group? [Y/Enter to continue]')
    if update_group == 'Y':
        group = validate_data('group')
        student['group'] = group

    # student_id
    update_student_id = input('Update student id? [Y/Enter to continue]')
    if update_student_id == 'Y':
        student_id = validate_data('student_id')
        student['id'] = student_id

    return student

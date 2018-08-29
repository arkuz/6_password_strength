import sys
import re
import getpass


def has_correct_length(password):
    length_password = 8
    if len(password) >= length_password:
        return True
    else:
        return False


def has_digit_symbol(password):
    if re.search('\d', password):
        return True
    else:
        return False


def has_lower_symbol(password):
    if re.search('[a-z,а-я]', password):
        return True
    else:
        return False


def has_upper_symbol(password):
    if re.search('[A-Z,А-Я]', password):
        return True
    else:
        return False


def has_special_symbol(password):
    if re.search('\W', password):
        return True
    else:
        return False


def get_password_strength(password):

    check_list = {
        (
            has_correct_length(password),
            'Password has less than 8 characters.',
        ),
        (
            has_digit_symbol(password),
            'Password does not contain a digit',
        ),
        (
            has_lower_symbol(password),
            'Password does not contain a lower symbol.',
        ),
        (
            has_upper_symbol(password),
            'Password does not contain a upper symbol.',
        ),
        (
            has_special_symbol(password),
            'Password does not contain a special symbol.',
        ),
    }

    password_complexity = 0
    cost_check = 2
    for check, _ in check_list:
        if check:
            password_complexity += cost_check

    return password_complexity, check_list


def print_check_result(complexity, check_list):
    print('Password complexity {0} out of 10.'.format(complexity))
    if complexity == 10:
        print('You have a strong password.')
    else:
        print('-' * 30)
        for check, message in check_list:
            if not check:
                print(message)


if __name__ == '__main__':
    password = getpass.getpass(prompt='Input your password: ')
    if not password:
        sys.exit('Password is empty.')

    complexity, check_list = get_password_strength(password)
    print_check_result(complexity, check_list)

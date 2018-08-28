import sys
import re


def has_correct_length(password):
    if len(password) >= 8:
        return True
    else:
        return 'Password has less than 8 characters.'


def has_digit_symbol(password):
    if re.match('^.*[0-9]+.*$', password):
        return True
    else:
        return 'Password does not contain a digit'


def has_lower_symbol(password):
    if re.match('^.*[a-z,а-я]+.*$', password):
        return True
    else:
        return 'Password does not contain a lower symbol.'


def has_upper_symbol(password):
    if re.match('^.*[A-Z,А-Я]+.*$', password):
        return True
    else:
        return 'Password does not contain a upper symbol.'


def has_special_symbol(password):
    if re.match('^.*[\W_]+.*$', password):
        return True
    else:
        return 'Password does not contain a special symbol.'


def get_password_strength(password):

    check_tuple = (
        has_correct_length(password),
        has_digit_symbol(password),
        has_lower_symbol(password),
        has_upper_symbol(password),
        has_special_symbol(password)
    )

    password_complexity = 0

    for check in check_tuple:
        if check is True:
            password_complexity += 2

    return password_complexity, check_tuple


def print_check_result(complexity, check_tuple):
    print('Password complexity {0} out of 10.'.format(str(complexity)))
    if complexity == 10:
        print('You have a strong password.')
    else:
        print('-' * 30)
        for check in check_tuple:
            if check is not True:
                print(check)


if __name__ == '__main__':
    password = input('Input your password: ')
    if not password:
        sys.exit('Password is empty.')

    complexity, check_tuple = get_password_strength(password)
    print_check_result(complexity, check_tuple)

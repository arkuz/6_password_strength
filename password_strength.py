import sys
import re
import getpass


def has_correct_length(password):
    length_password = 8
    return len(password) >= length_password


def has_digit_symbol(password):
    return bool(re.search('\d', password))


def has_lower_symbol(password):
    return bool(re.search('[a-z,а-я]', password))


def has_upper_symbol(password):
    return bool(re.search('[A-Z,А-Я]', password))


def has_special_symbol(password):
    return bool(re.search('\W', password))


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
    message_list = []
    for check, message in check_list:
        if check:
            password_complexity += cost_check
        else:
            message_list.append(message)

    return password_complexity, message_list


def print_check_result(complexity, message_list):
    print('Password complexity {0} out of 10.'.format(complexity))
    if complexity == 10:
        print('You have a strong password.')
    else:
        print('-' * 30)
        for message in message_list:
            print(message)


if __name__ == '__main__':
    password = getpass.getpass(prompt='Input your password: ')
    if not password:
        sys.exit('Password is empty.')

    complexity, message_list = get_password_strength(password)
    print_check_result(complexity, message_list)

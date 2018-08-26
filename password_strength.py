import sys
import re


def get_password_strength(password):
    check_list = {
        'len_pass': False,
        'digit_symbol': False,
        'lower_symbol': False,
        'upper_symbol': False,
        'special_symbol': False,
    }

    message = ''

    if re.match("^.*[А-я]+.*$", password):
        sys.exit('Password must not contain russian characters.')

    if len(password) >= 8:
        check_list['len_pass'] = True
    else:
        message += 'Password has less than 8 characters. \n'

    if re.match("^.*[0-9]+.*$", password):
        check_list['digit_symbol'] = True
    else:
        message += 'Password does not contain a digit. \n'

    if re.match("^.*[a-z]+.*$", password):
        check_list['lower_symbol'] = True
    else:
        message += 'Password does not contain a lower symbol. \n'

    if re.match("^.*[A-Z]+.*$", password):
        check_list['upper_symbol'] = True
    else:
        message += 'Password does not contain a upper symbol.  \n'

    if re.match("^.*[\W_]+.*$", password):
        check_list['special_symbol'] = True
    else:
        message += 'Password does not contain a special symbol. \n'

    check_cost = int(10 / len(check_list))
    password_complexity = 0

    for check in check_list:
        if check_list[check]:
            password_complexity += check_cost

    return password_complexity, message


def print_check_result(complexity, message):
    print('Password complexity {0} out of 10.'.format(str(complexity)))
    if complexity < 10:
        print('-' * 30)
        print('Best practices for password strength: \n' + message)
    else:
        print('You have a strong password.')


if __name__ == '__main__':
    password = input('Input your password: ')
    if not password:
        sys.exit('Password is empty.')
    complexity, message = get_password_strength(password)
    print_check_result(complexity, message)

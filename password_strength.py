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

    if len(password) >= 8:
        check_list['len_pass'] = True
    else:
        message = 'Password has less than 8 characters'
        
    if re.match("^.*[0-9]+.*$", password):
        check_list['digit_symbol'] = True

    if re.match("^.*[a-z]+.*$", password):
        check_list['lower_symbol'] = True

    if re.match("^.*[A-Z]+.*$", password):
        check_list['upper_symbol'] = True

    if re.match("^.*[\W_]+.*$", password):
        check_list['special_symbol'] = True

    check_cost = int(10 / len(check_list))
    password_complexity = 0

    for check in check_list:
        print(check + " : " + str(check_list[check]))
        if check_list[check]:
            password_complexity += check_cost

    return password_complexity, message


if __name__ == '__main__':

    password = input('Ipput your password: ')

    if not password:
        sys.exit('Password is empty.')

    complexity, message = get_password_strength(password)

    print(str(complexity) + ' ' + message)
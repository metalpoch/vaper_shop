from datetime import date
from random import randint


def birth_date_valid(birth_date):
    '''
    This function if the age of user is under 21
    '''
    return True if (date.today() - birth_date).days / 365 > 21 else False


def basic_math():
    '''
    This function generate a simple math problem
    '''
    num1, num2, oper = randint(1, 10), randint(1, 10), randint(1, 3)
    if oper == 1:
        oper = '+'
        result = num1 + num2
    elif oper == 2:
        oper = '-'
        result = num1 - num2
    else:
        oper = '*'
        result = num1 * num2
    return num1, num2, oper, result


def no_have_credits(credits, product_price, quantity):
    '''
    This function validate if the client have credits
    '''
    return True if credits < (product_price * quantity) else False

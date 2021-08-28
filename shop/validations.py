from datetime import date


def birth_date_valid(birth_date):
    return True if (date.today() - birth_date).days / 365 > 18 else False
    # age = (date.today() - age).days / 365
    # if age > 18:
    #     return True
    # else:
    #     return False

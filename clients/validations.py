from datetime import date


def birth_date_valid(birth_date):
    return True if (date.today() - birth_date).days / 365 > 18 else False

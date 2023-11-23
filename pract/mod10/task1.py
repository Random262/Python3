import re
import doctest


def correctpass(password: str) -> bool:
    """
    Функция проверяет корректность пароля
    :param password: входящая строка
    :returns: (bool) Подходит ли пароль

    Примеры:

    >>> correctpass("rtG3FG!Tr^e")
    True
    >>> correctpass("aA1!*!1Aa")
    True
    >>> correctpass("oF^a1D@y5e6")
    True
    >>> correctpass("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> correctpass("пароль")
    False
    >>> correctpass("password")
    False
    >>> correctpass("qwerty")
    False
    >>> correctpass("lOngPa$$$W0Rd")
    False
    """
    if not re.match(r'^[0-9A-Za-z^$%@#&*!?]{6,}$', password):
        return False  # от 0 до 9, от A до z, спец знаки, от 6 знаков
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False  # не найдено больше двух заглавных лат букв
    if not re.search(r'[0-9]', password):
        return False  # не найдено ни одной цифры
    if len(set(re.findall(r'[^a-zA-Z0-9]',  password))) < 2:
        return False  # не найдено два различных символа кроме лат букви, цифр
    if re.search(r'(.)\1\1', password):
        return False  # не найдено три одинаковых символа
    return True


doctest.testmod()

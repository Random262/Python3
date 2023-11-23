import re
import doctest

patternRGB = (
    r'^rgb\('
    r'(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|100%|[1-9]?\d%),\s*'
    r'(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|100%|[1-9]?\d%),\s*'
    r'(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|100%|[1-9]?\d%)'
    r'\)$'
)
# rgb(от 0 до 99 | 1, две цифры | 2, от 0 до 4, от 0 до 9 | 25, от 0 до 5 |
# 100% | возможно от 1 до 9, от 0 до 9, любое кол-во пробелов [три раза])
patternHEX = r'^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})$'
# #любые 6 знаков из 0-9 A-F a-f | любые 3 знака из 0-9 A-F a-f
patternHSL = (
    r'^hsl\('
    r'(\d{1,2}|1\d{2}|2\d{2}|3[0-5]\d|360),\s*'
    r'(100%|[1-9]?\d%),\s*(100%|[1-9]?\d%)\)$'
)
# hsl(от 0 до 99 | 1, две цифры | 2, две цифры | 3, от 0 до 5, от 0 до 9 | 360 |
# 100% | возможно от 1 до 9, от 0 до 9, любое кол-во пробелов [два раза])


def correctcolor(color: str) -> bool:
    """
    Функция проверяет корректность введенного цвета
    :param color: входящая строка
    :return: (bool) Правильный ли формат цвета

    Примеры:

    >>> correctcolor("#21f48D")
    True
    >>> correctcolor("#888")
    True
    >>> correctcolor("rgb(255, 255,255)")
    True
    >>> correctcolor("rgb(10%, 20%, 0%)")
    True
    >>> correctcolor("hsl(200,100%,50%)")
    True
    >>> correctcolor("hsl(0, 0%, 0%)")
    True
    >>> correctcolor("#2345")
    False
    >>> correctcolor("ffffff")
    False
    >>> correctcolor("rgb(257, 50, 10)")
    False
    >>> correctcolor("hsl(20, 10, 0.5)")
    False
    >>> correctcolor("hsl(34%, 20%, 50%)")
    False
    """
    if (re.match(patternRGB, color) or
            re.match(patternHEX, color) or
            re.match(patternHSL, color)):
        return True
    return False


doctest.testmod()


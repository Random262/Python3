import functools

memo_dict = dict()


def memoize(func):
    @functools.wraps(func)
    def wrapped_func(n):
        if n not in memo_dict.keys():
            memo_dict[n] = func(n)
        return memo_dict[n]
    return wrapped_func


@memoize
def fibonacci(n):
    '''Рекурсивная функция Фибоначчи'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i), end=' ')
print()
print(fibonacci.__doc__)
print(fibonacci.__name__)


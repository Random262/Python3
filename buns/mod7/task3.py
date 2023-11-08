import functools
import time

memo_dict = dict()


def memoize(func):
    @functools.wraps(func)
    def wrapped_func(n):
        if n not in memo_dict.keys():
            memo_dict[n] = func(n)
        return memo_dict[n]
    return wrapped_func


def timer(func):
    @functools.wraps(func)
    def wrapped_func(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(round(end - start, 4), end = " ")
        wrapped_func.timerflag = True
        return result
    return wrapped_func


@memoize
@timer
def fibonacci(n):
    '''Рекурсивная функция Фибоначчи'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timer
def slowfibonacci(n):
    '''Рекурсивная функция Фибоначчи'''
    if n < 2:
        return n
    return slowfibonacci(n - 1) + slowfibonacci(n - 2)


print(slowfibonacci(28))
print(fibonacci(28))
print()
print(fibonacci.__doc__)
print(fibonacci.__name__)


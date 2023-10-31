def make_num_list(a):
    arr = []
    for i in str(a):
        arr.append(int(i))
    return arr


def make_armstrong_gen():
    for i in range(1, 1000000):
        l = len(str(i))
        if i == sum(((int(x)**l) for x in make_num_list(i))):
            yield i


gen = make_armstrong_gen()


def get_armstrong_numbers():
    return next(gen)


for i in range(18):
    print(get_armstrong_numbers(), end=' ')

# Ожидаемый результат кода:
# 1 153 370 407 1634 8208 9474 54748

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


a = [int(i) for i in input().split()]
print(gcd(a[0], a[1]))

def newpow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return newpow(a**2, n // 2)
    else:
        return a * newpow(a, n - 1)


arr = [int(i) for i in input().split()]
print(newpow(arr[0], arr[1]))

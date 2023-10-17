a = [int(i) for i in input().split()]
lenSetA = len(set(a))
if lenSetA == 1:
    print('Все числа равны')
elif lenSetA == len(a):
    print('Все числа разные')
else:
    print('Есть равные и неравные числа')
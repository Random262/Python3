a = input()
arr = list(set(a))
flag, flagAns = False, False
ans, oddStr = '', ''
for i in arr:
    n = a.count(i)
    if n % 2 == 0:
        ans += i * (n // 2)
    elif not flag:
        oddStr = i * n
        flag = True
    else:
        flagAns = True
        break
if not flagAns:
    print(ans + oddStr + ans[::-1])
else:
    print('Нельзя составить палиндром')

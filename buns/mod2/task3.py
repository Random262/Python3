strA = input()
a, b, c = '', '', ''
flag1 = False
flag2 = False
maxi = ''
for i in strA:
    if flag1 and not flag2:
        if i in '0123456789-':
            b += i 
    elif flag2:
        if i in '0123456789-':
            c += i
    elif i in '0123456789-':
        a += i
    if i == ' ' and flag1 == True:
        flag2 = True 
    if i == ' ':
        flag1 = True
a, b, c = int(a), int(b), int(c)
if (b >= a >= c) or (b <= a <= c):
    print(a)
elif (a >= b >= c) or (a <= b <= c):
    print(b)
else:
    print(c)




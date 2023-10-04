string = input()
a, b = '', ''
flag = False
for i in string:
    if flag:
        if i in '0123456789.':
            b += i  
    elif i in '0123456789.':
        a += i
    if i == ' ':
        flag = True
ans = float(a) % float(b)        
if int(ans) == float(ans):
    print(int(ans))
else:
    print(ans)

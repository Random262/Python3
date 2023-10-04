a = float(input())
print('%.2f' % (a * 4),'%.2f' % (a * a), sep = ', ', end = ', ')
d = ''
flag = False
counter = 0
last = ''
second_last = ''
for i in str(a * (2 ** (1/2))):
    last = i
    if flag:
        counter += 1
    if flag and counter == 3:
        break    
    d += i
    second_last = i
    if  i == '.':
        flag  = True   
if int(last) >= 5:
    print('%.2f' % (float(d) + 0.01))
else:
    print('%.2f' % float(d))
    


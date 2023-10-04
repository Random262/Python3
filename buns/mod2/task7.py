a = input()
counter1 = 0
counter0 = 0
for i in a:
    if i == '1':
        counter1 += 1
    elif i == '0':
        counter0 += 1
if counter1 == counter0:
    print('yes')
else:
    print('no')

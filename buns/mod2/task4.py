flag = True
while flag:
    a = ''
    strA = input()
    counter = 0
    dot = 0
    for i in strA:
        if i in '0123456789':
            a += i
        elif i == '.' and dot == 0:
            a += i
            dot += 1
        else:
            counter += 1
    if counter == 0:
        a = float(a)
        if (int(a) == float(a) and int(a) > 0):
            flag = False
            a = int(a)
        else:
            print('Неверный ввод')
    else:
        print('Неверный ввод')
        
number = a
newNumber = ''
while number > 0:
    part = number % 2
    newNumber = str(part) + newNumber
    number = number // 2
print(newNumber, end = ', ')

number = a
newNumber = ''
while number > 0:
    part = number % 8
    newNumber = str(part) + newNumber
    number = number // 8
print(newNumber, end = ', ')

number = a
newNumber = ''
while number > 0:
    part = number % 16
    number = number // 16
    if part > 9:
        part = 'ABCDEF'[part - 10]
    newNumber = str(part) + newNumber
print(newNumber)

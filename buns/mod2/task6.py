strA = input() + '.'
answer = ''
a = ''
for i in strA:    
    if i == '.':        
        answer = a + ' ' + answer
        a = ''
    else:
        a += i
a = ''
for i in answer:
    if i == ' ':
        print(a)
        a = ''
    else:
        a += i


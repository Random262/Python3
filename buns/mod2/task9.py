a = input()
vow = 0
con = 0
for i in a:
    if i in 'бвгджзйклмнпрстфхцчшщ':
        con += 1
    elif i in 'аиоуыэеёюя':
        vow += 1
print(vow, con)        
    

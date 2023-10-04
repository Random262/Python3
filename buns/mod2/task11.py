a = input()
ans = False
same = ''
for i in a:
    if i in '0123456789':
        if i in same:
            ans = True
            break
        else:
            same += i            
print(ans)            
    

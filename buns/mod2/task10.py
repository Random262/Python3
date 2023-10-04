a = input() + ' '
last = ''
ans = ''
for i in a:
    if i == ' ':
        ans += last
    last = i
print(ans)     
    

a = input()
even = 0
odd = 0
counter = 1
for i in a:
    if counter % 2 == 1:
        odd += int(i)
    else:
        even += int(i)
    counter += 1            
if (odd + even * 3) % 10 == 0:
    print('yes')
else:
    print('no')

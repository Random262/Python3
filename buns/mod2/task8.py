strA = input()
a = strA[-1:]
s = strA[:-2]
counter = 0
for i in s:
    if a == i:
        counter += 1
    else:
        break
print(counter)

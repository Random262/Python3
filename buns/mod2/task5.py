strA = input()
a = strA[0]
shift = int(strA[2:])
place = ord(a)
if shift >= 0:
    shift %= 26
else:
    shift %= -26
place += shift
if place < 97:
    place += 26
elif place > 122:
    place -= 26
print(chr(place))
        
    

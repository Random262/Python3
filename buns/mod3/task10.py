size = int(input())
first = ', '.join([str(i) for i in range(1, size + 1)])
[print(first) for i in range(size)]
print()
[print(', '.join([str(i)]*size)) for i in range(1, size + 1)]
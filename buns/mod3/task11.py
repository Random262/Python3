k = int(input())
arr, diag1, diag2 = [], [], []
for i in range(k):
    arr.append(list(input()))
ans = arr[:]
for i in range(k):
    ans.append([x[i] for x in arr])
    for j in range(k):
        if i == j:
            diag1.append(arr[i][j])
        if j == k - 1 - i:
            diag2.append(arr[i][j])
ans.append(diag1)
ans.append(diag2)

flag = True
for i in ans:
    k = len(set(i))
    if  k == 1 and 'X' in i:
        print('X')
        flag = False
        break
    elif k == 1 and 'O' in i:
        print('O')
        flag = False
        break
if flag:
    print('Ничья')
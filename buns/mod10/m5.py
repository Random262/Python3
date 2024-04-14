def find_insert_position(A, x):
    left, right = 0, len(A)
    while left < right:
        mid = left + (right - left) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


A = [1, 2, 3, 3, 3, 5]
x = 4
assert find_insert_position(A, x) == 5

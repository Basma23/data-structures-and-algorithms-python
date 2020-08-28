def BinarySearch(arr, n):
    a = 0
    b = len(arr) - 1
    while a <= b:
        i = (a + b)//2
        if arr[i] == n:
            return i
        elif arr[i] < n:
            a = i + 1
        elif arr[i] > n:
            b = i - 1
    return -1

print(BinarySearch([4,8,15,16,23,42], 42))
print(BinarySearch([11,22,33,44,55,66,77], 90))
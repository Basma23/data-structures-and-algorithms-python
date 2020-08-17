def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    return arr[::-1]
inputs = reverse_array([1, 2, 3, 4, 5, 6])
print(inputs)
arr = [89, 2354, 3546, 23, 10, -923, 823, -12]
print(arr[::-1])
array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
for i in reversed(array):
    print(i)

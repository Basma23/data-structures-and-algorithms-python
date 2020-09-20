def insertionSort(arr):
   for i in range(1, len(arr)):
       current = arr[i]
       while i > 0 and arr[i-1] > current:
           arr[i] = arr[i-1]
           i = i-1
           arr[i] = current
   return arr

if __name__ == '__main__':
    arr_list = [5, 2, 1, 9, 0, 4, 6]
    print(insertionSort(arr_list))
    assert insertionSort([5, 2, 1, 9, 0, 4, 6]) == [0, 1, 2, 4, 5, 6, 9]
    print('The test is pass :)')

def partition(arr, low, high): 
    i = (low - 1)         
    pivot = arr[high]    
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i + 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 

def quick_sort(arr, low, high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quick_sort(arr, low, pi - 1) 
        quick_sort(arr, pi + 1, high) 
    return arr

if __name__ == "__main__":
    arr = [8, 4, 23, 42, 16, 15]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
    assert quick_sort(arr, 0, n - 1) == [4, 8, 15, 16, 23, 42]
    print('Test passed :)')
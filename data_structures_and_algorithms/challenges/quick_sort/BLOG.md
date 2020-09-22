# Quick Sort

[Quick sort](https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm) is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.

Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. This algorithm is quite efficient for large-sized data sets as its average and worst-case complexity are O(nLogn) and image.png(n2), respectively.

## Pseudocode

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
## Trace

Sample Array: ```[8, 4, 23, 42, 16, 15]```

First pass ---> ```[8, 4, 15, 42, 16, 23]```

The pivot selected which is 23 and we moved it to the end of the array

Second pass ---> ```[8, 4, 15, 16, 42, 23]```

Then we partitioned the subarray, then we moved the left bound to the right until it reached a value greater than or equal to the pivot, then we moved the right bound to the left until it crossed the left bound or found a value less than the pivot, then we swaped the selected values.

Third pass ----> ```[8, 4, 15, 16, 23, 42]```

Then we moved the left bound to the right until it reached a value greater than or equal to the pivot, the bounds have crossed, which means that all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot, so, we move the pivot which is 42 to the end of the array.

Fourth pass ---> ```[8, 16, 15, 4, 23, 42]```

Then we call ```quick_sort``` on the left sublist, then we selected the pivot again which is 4, and we moved it to its end location on the array. 

Fifth pass ----> ```[4, 16, 15, 8, 23, 42]```

Then we partitioned the subarray, and moved the left bound to the right until it reaches a value greater than or equal to the pivot, then we moved the right bound to the left until it crossed the left bound or found a value less than the pivot, then the bounds have crossed which means that all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot, so, we move the pivot which is 8 to location on the array.

Sixth pass ----> ```[4, 16, 8, 15, 23, 42]```

Then we call ```quick_sort``` on the right sublist, then we selected the pivot again which is 15, and we moved it to the end.

Seventh pass ---> ```[4, 8, 15, 16, 23, 42]```

Then we partitioned the subarray, and moved the left bound to the right until it reaches a value greater than or equal to the pivot, 16 is grater than pivot, then we swap the selected values, then we moved the left bound to the right until it reached a value greater than or equal to the pivot, then we moved the right bound to the left until it crossed the left bound or found a value less than the pivot, then the bounds have crossed which means that all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot, so, we move the pivot which is 16 to its end location on the array.

Eighth pass ---> ```[4, 8, 15, 16, 23, 42]```

Now left sublist contains a single element which means it is sorted, then the right sublist which contains a single element which means it is sorted, then the sort is done.

## Efficency

- **Time:** O(n^2)
- **Space:** O(log(n))
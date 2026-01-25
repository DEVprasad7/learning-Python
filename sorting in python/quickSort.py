def quickSort(arr , l, r):
    if (l < r):
        p = parttion(arr, l, r)
        
        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)
    
def parttion(arr, l, r):
    pivot = arr[l]
    i = l + 1
    j = r
    
    while True:
        while ( i <= j and arr[i] < pivot ):
            i = i + 1
            
        while ( i <= j and arr[j] > pivot):
            j = j - 1
            
        if ( i < j):
            arr[i], arr[j] = arr[j], arr[i]
            
        else:
            break
        
    arr[l], arr[j] = arr[j], arr[l]
    
    return j

arr = [65,42,31,67,88,2,56,3,1]

quickSort(arr, 0, len(arr)-1)

print(arr)
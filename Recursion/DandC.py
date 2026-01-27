# Divide and conquer


def min_max(arr, start, end):
    if (start == end):
        return arr[start], arr[end]
    
    if ((start+1) == end):
        if (arr[start] < arr[end]):
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
        
    mid = (start + end) // 2
    
    min1, max1 = min_max(arr, start, mid)
    min2, max2 = min_max(arr, mid+1, end)
    
    return min(min1, min2), max(max1, max2)

arr = [1000, 11, 445, 1, 330, 3000]
mn, mx = min_max(arr, 0, len(arr)-1)
print(f"Minimum element is : {mn}")
print(f"Maximum element is : {mx}")
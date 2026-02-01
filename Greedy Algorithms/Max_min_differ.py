def Max_Min_D(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    minn = maxx = 0
    j = n-1
    
    for i in range(0, mid):
        maxx += abs(arr[i] - arr[j])
        
        j -= 1
        minn += abs(arr[2*i] - arr[(2*i)+1])
        
        
    return maxx, minn

arr = [12,5,25,10,2,8,15,30]

maxx, minn = Max_Min_D(arr)
print("Maximum Difference: ", maxx)
print("Minimum Difference: ", minn)
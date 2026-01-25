class Array:
    def __init__(self):
        self.arr = []
        
    def insert(self, v):
        self.arr.append(v)
        
    def length(self):
        return len(self.arr)
        
    def display(self):
        print(self.arr)
        
    def remove(self, v):
        if v in self.arr:
            self.arr.remove(v)
            
            
    def quick_sort(self, reverse=False):
        
        def quickSort(arr, l, r):
            if (l<r):
                pivot = parttion(arr, l, r)
                quickSort(arr, l, pivot-1)
                quickSort(arr, pivot+1, r)
                
        def parttion(arr, l, r):
            pivot = l
            i = l+1
            j = r
            
            if not reverse:
                while True:
                    while ( i<=j and arr[i] < arr[pivot]):
                        i = i+1
                        
                    while ( i<=j and arr[j] > arr[pivot]):
                        j = j-1
                        
                    if(i<j):
                        arr[i], arr[j] = arr[j], arr[i]
                        
                    else:
                        break
                arr[pivot], arr[j] = arr[j], arr[pivot]
                return j
            
            else:
                while True:
                    while ( i<=j and arr[i] > arr[pivot]):
                        i = i+1
                        
                    while ( i<=j and arr[j] < arr[pivot]):
                        j = j-1
                        
                    if(i<j):
                        arr[i], arr[j] = arr[j], arr[i]
                        
                    else:
                        break
                arr[pivot], arr[j] = arr[j], arr[pivot]
                return j
                
        
        quickSort(self.arr, 0, len(self.arr)-1)
            
arr = Array()

l = [64,12,32,43,54,20,15,2,1]

for i in l:
    arr.insert(i)


arr.display()

arr.quick_sort()
arr.display()

arr.quick_sort(reverse=True)
arr.display()
                
                
                

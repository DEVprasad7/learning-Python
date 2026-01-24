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
            
            
    def merge_sort(self, reverse=False):
        
        def Divide(arr, l, r):
            if (l < r):
                m = (l+r) // 2
                Divide(arr, l, m)
                Divide(arr, m+1, r)
                merge(arr, l, m, r)
                
        def merge(arr, l, m, r):
            s1 = m - l + 1
            s2 = r - (m+1) + 1
            
            L = [0] * s1
            R = [0] * s2
            
            for i in range(0, s1):
                L[i] = arr[l + i]
                
            for j in range(0, s2):
                R[j] = arr[m + 1 + j]
                
            i = j = 0
            k = l
            
            while (i < s1 and j < s2):
                if not reverse:
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                        
                    else:
                        arr[k] = R[j]
                        j += 1
                        
                    k += 1
                else:
                    if L[i] > R[j]:
                        arr[k] = L[i]
                        i += 1
                        
                    else:
                        arr[k] = R[j]
                        j += 1
                        
                    k += 1
                    
            while (i < s1):
                arr[k] = L[i]
                i += 1
                k += 1
                
            while (j < s2):
                arr[k] = R[j]
                j += 1
                k += 1
                
        Divide(self.arr, 0, len(self.arr)-1)
            
arr = Array()

l = [64,12,32,43,54,20,15,2,1]

for i in l:
    arr.insert(i)


arr.display()

arr.merge_sort()
arr.display()

arr.merge_sort(reverse=True)
arr.display()
                
                
                

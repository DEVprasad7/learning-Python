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
            
            
    def selection_sort(self, reverse=False):
        rn = len(self.arr)
        
        if reverse == False:
            for i in range(rn):
                min = i
                for j in range(i, rn):
                    if (self.arr[min] > self.arr[j]):
                        min = j
                        
                self.arr[i], self.arr[min] = self.arr[min], self.arr[i]
        else:
            for i in range(rn):
                max = i
                for j in range(i, rn):
                    if (self.arr[max] < self.arr[j]):
                        max = j
                        
                self.arr[i], self.arr[max] = self.arr[max], self.arr[i]
                
arr = Array()

l = [64,12,32,43,54,20,15,2,1]

for i in l:
    arr.insert(i)


arr.display()

arr.selection_sort()
arr.display()

arr.selection_sort(reverse=True)
arr.display()
                
                
                

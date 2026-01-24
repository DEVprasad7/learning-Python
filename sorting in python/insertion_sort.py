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
            
            
    def insertion_sort(self, reverse=False):
        rn = len(self.arr)
        for i in range(1, rn):
            key = self.arr[i]
            j = i-1
            
            if not reverse:
                while (j>=0 and key < self.arr[j]):
                    self.arr[j+1] = self.arr[j]
                    j = j-1
        
                self.arr[j+1] = key
                
            else:
                while(j>=0 and key > self.arr[j]):
                    self.arr[j+1] = self.arr[j]
                    j = j-1
                
                self.arr[j+1] = key
                
            
arr = Array()

l = [64,12,32,43,54,20,15,2,1]

for i in l:
    arr.insert(i)


arr.display()

arr.insertion_sort()
arr.display()

arr.insertion_sort(reverse=True)
arr.display()
                
                
                

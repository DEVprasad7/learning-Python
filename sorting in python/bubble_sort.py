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
            
            
    def bubble_sort(self, reverse=False):
        a = self.arr
        rn = len(a)
        
        if reverse == False:
            for i in range(0, rn):
                for j in range(0, rn-i-1):
                    if (a[j] > a[j+1]):
                        a[j], a[j+1] = a[j+1], a[j]
                        
        else:
            for i in range(0, rn):
                for j in range(0, rn-i-1):
                    if (a[j] < a[j+1]):
                        a[j], a[j+1] = a[j+1], a[j]
                        
                        
                        
arr = Array()

l = [64,12,32,43,54,20,15]

for i in l:
    arr.insert(i)
    
arr.display()
arr.bubble_sort(reverse=True)
arr.display()
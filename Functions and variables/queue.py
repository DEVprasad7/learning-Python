class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, v):
        self.items.append(v)
        
    def remove(self, v):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        
        if v not in self.items:
            raise Exception("Value not found in queue")
        else:
            self.items.remove(v)
            
    def delete(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        else:
            self.items.pop(0)
            
    def print(self):
        print(self.items)
        
    def size(self):
        return len(self.items)
    
queue = Queue()

L = [1,2,3,4,5,6,7,8,9,0]

for i in L:
    queue.insert(i)
    
queue.print()
print("Size:", queue.size())

for i in range(queue.size()):
    queue.delete()
    
queue.print()
print("Size:", queue.size())
print(queue.isEmpty())
        
        
        
        
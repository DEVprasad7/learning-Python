class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, v):
        self.stack.insert(0, v)
        
    def pop(self):
        if (self.isEmpty()):
            raise Exception("Stack is empty")
        else:
            return self.stack.pop(0)
        
    def peek(self):
        if (self.isEmpty()):
            raise Exception("Stack is empty")
        else:
            return self.stack[0]
        
    def print(self):
        print(self.stack)
        
    def size(self):
        return len(self.stack)
    

stack = Stack()

L = [1,2,3,4,5,6,7,8,9,0]
for i in L:
    stack.push(i)

stack.print()
print(stack.peek())
print("Size:", stack.size())

print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print()
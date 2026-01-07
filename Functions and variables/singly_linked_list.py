class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, start=False):
        temp = Node(value)
        
        if self.head == None:
            self.head = temp
            return
        
        if start == True:
            temp.next = self.head
            self.head = temp
            return
        else:
            
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp
            return
        
    def insert_after(self, value, after):
        if self.head == None:
            return "List is Empty"
        
        temp = Node(value)
        curr = self.head
        
        while True:
            if curr.data == after:
                temp.next = curr.next
                curr.next = temp
                return
            if curr.next == None:
                return "Cannot Insert After Value Not Found"
            curr = curr.next
    
    def remove(self, value):
        if self.head == None:
            return "List is Empty"
        
        temp = self.head
        prev = temp
        if temp.data == value:
            self.head = temp.next
            return
        
        while True:
            if temp.data == value:
                prev.next = temp.next
                return
            if temp.next == None:
                return "Not Found"
            prev = temp
            temp = temp.next

    def show(self):
        if self.head == None:
            return "List is Empty"
        
        curr = self.head
        while True:
            if curr.next == None:
                print(curr.data)
                break
            print(curr.data, end=" -> ")
            curr = curr.next
            
LL = SinglyLinkedList()

while True:
    print("\n1. Insert Element At Start\n2. Insert Element At End\n3. Insert After Element\n4. Remove Element\n5. Show Elements\n6. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value to insert at start: "))
        LL.insert(val, start=True)
    elif ch == 2:
        val = int(input("Enter value to insert at end: "))
        LL.insert(val)
    
    elif ch == 3:
        val = int(input("Enter value to insert: "))
        af = int(input("Enter value after which to insert: "))
        LL.insert_after(val, af)
    
    elif ch == 4:
        LL.remove(int(input("Enter value to remove: ")))
    
    elif ch == 5:
        LL.show()
    else:
        break
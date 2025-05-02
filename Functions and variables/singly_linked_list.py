class Node:
    # A node in a singly linked list contains data and a pointer to the next node.
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer set to None.
        self.head = None

    def add_at_start(self, data):
        # Add a new node with the given data at the start of the list.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        # Add a new node with the given data at the end of the list.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def add_at_position(self, pos, data):
        # Add a new node with the given data at the specified position in the list.
        if pos == 0:
            self.add_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def remove_from_start(self):
        # Remove the node at the start of the list.
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def remove_from_end(self):
        # Remove the node at the end of the list.
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        prev = self.head
        while prev.next and prev.next.next:
            prev = prev.next
        prev.next = None

    def remove_by_position(self, pos):
        # Remove the node at the specified position in the list.
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.remove_from_start()
            return
        current = self.head
        count = 0
        while current.next and count < pos - 1:
            current = current.next
            count += 1
        if not current.next:
            print("Position out of range")
            return
        current.next = current.next.next

    def remove_by_value(self, value):
        # Remove the first node with the specified value from the list.
        if not self.head:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Value not found")

    def display_list(self):
        # Display the elements of the list.
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage

def main():
    ll = LinkedList()
    
    print('-----------------------------------------------------------------------------------------------------------------------')
    
    
    try:
        while True:
            choice = int(input("1 -> ADD ELEMENT AT START \n2 -> ADD ELEMENT AT END \n3 -> ADD ELEMENT AT POSITION \n4 -> REMOVE ELEMENT FROM START \n5 -> REMOVE ELEMENT FROM END \n6 -> REMOVE ELEMENT FROM INDEX \n7 -> REMOVE ELEMENT BY VALUE \n8 -> DISPLAY LIST \n9 -> QUIT \nCHOOSE :"))

            if choice == 1:
                data = input("Enter data to add at start: ")
                ll.add_at_start(data)
            elif choice == 2:
                data = input("Enter data to add at end: ")
                ll.add_at_end(data)
            elif choice == 3:
                pos = int(input("Enter position to add: "))
                data = input("Enter data to add at position: ")
                ll.add_at_position(pos, data)
            elif choice == 4:
                ll.remove_from_start()
            elif choice == 5:
                ll.remove_from_end()
            elif choice == 6:
                pos = int(input("Enter index to remove: "))
                ll.remove_by_position(pos)
            elif choice == 7:
                value = input("Enter value to remove: ")
                ll.remove_by_value(value)
            elif choice == 8:
                ll.display_list()
            elif choice == 9:
                print("Exiting...")
                break
            else:
                print("Invalid Input")
                return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return    
    
    print('-----------------------------------------------------------------------------------------------------------------------')

if __name__ == "__main__":
    main()
# The above code implements a singly linked list with various operations such as adding, removing, and displaying elements.

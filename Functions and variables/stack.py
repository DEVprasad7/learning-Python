
def push(stack, top, item, MAX):
    top += 1
    stack[top] = item
    return stack, top

def pop(stack, top):
    item = stack[top]
    top -= 1
    return stack, top, item

def display(stack, top):
    if top == 0:
        print("Stack is empty")
    else:
        for i in range(1, top+1):
            print(stack[i], end=" ")
        print()

def display_top(stack, top):
    if top == 0:
        print("Stack is empty")
    else:
        print(stack[top])

def main():
    MAX = int(input("Enter the size of the stack: "))
    stack = [0] * (MAX + 1) 
    top = 0
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Display top")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            if top == MAX:
                print("Stack is full")
            else:
                item = int(input("Enter the item to be pushed: "))
                stack, top = push(stack, top, item, MAX)
        elif choice == 2:
            if top == 0:
                print("Stack is empty")
            else:
                stack, top, item = pop(stack, top)
                print("Popped item is", item)
        elif choice == 3:
            display(stack, top)
        elif choice == 4:
            display_top(stack, top)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
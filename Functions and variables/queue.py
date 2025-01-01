def push_item(queue, item, max_length):
    if len(queue) >= max_length:
        print("Queue is full")
    else:
        item = int(input("Enter the item to push: "))
        queue.append(item)


def pop_item(queue):
    if not queue:
        print("Queue is empty")
    else:
        print("Popped item is: ", queue.pop(0))

def pop_item_specific(queue, item):
    if not queue:
        print("Queue is empty")
    else:
        item = int(input("Enter the item to pop: "))
        if item in queue:
            queue.remove(item)
        else:
            print("Item not found in the queue")

def view_queue(queue):
    print(queue)

def main():
    queue = []
    max_length = int(input("Enter the max length of the queue: "))
    item = 0
    while True:
        choice = int(input("Enter 1 to push, 2 to pop, 3 to pop specific item, 4 to view queue and 5 to quit: "))
        if choice == 1:
            push_item(queue, item, max_length)
        elif choice == 2:
            pop_item(queue)
        elif choice == 3:
            pop_item_specific(queue, item)
        elif choice == 4:
            view_queue(queue)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

    
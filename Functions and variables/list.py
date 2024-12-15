
def add_to_list(n):

    element = int(input("Enter the element : "))
    n.append(element)

def remove_from_list(n):

    element = int(input("Enter the element to remove from list : "))
    if element in n:
        n.remove(element)
    else:
        print("Element not present in the list..!")

def print_list(n):
    print(n)


def sort_list(n):
    n = sorted(n)
    print(n)

def main():
    start = True
    l = []
    while start:

        choice = int(input("1 -> ADD ELEMENT \n2 -> POP ELEMENT \n3 -> PRINT LIST \n4 -> SORT LIST \n5 -> EXIT \nCHOOSE :"))

        if choice == 1:
            add_to_list(l)
        elif choice == 2:
            remove_from_list(l)
        elif choice == 3:
            print_list(l)
        elif choice == 4:
            sort_list(l)
        elif choice == 5:
            start = False
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
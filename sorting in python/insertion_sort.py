# sorting a list using insertion sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

try:
    n = int(input("Enter the number of elements in the list: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Enter {n} elements:")
        numbers = []
        for _ in range(n):
            while True:
                try:
                    num = int(input())
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
        
        print(f"Original list: {numbers}")

        insertion_sort(numbers)
        print(f"Sorted list: {numbers}")
except ValueError:
    print("Invalid input! Please enter a valid integer for the number of elements.")



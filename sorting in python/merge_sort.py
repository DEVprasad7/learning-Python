# Sorting a list using merge sort algorithm

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

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

        merge_sort(numbers)
        print(f"Sorted list: {numbers}")
except ValueError:
    print("Invalid input! Please enter a valid integer for the number of elements.")

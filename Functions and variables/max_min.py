def main():
    print("This program finds the largest and the smallest number.")
    n = int(input("How many numbers are there? "))
    max = float(input("Enter a number >> "))
    min = max
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > max:
            max = x
        if x < min:
            min = x
    print("The largest value is", max)
    print("The smallest value is", min)

if __name__ == '__main__':
    main()
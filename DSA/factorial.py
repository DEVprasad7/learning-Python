# Factorial calculation using recursion

def fact(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n - 1)

def fact_seq(n):
    for i in range(n + 1):
        print(f"Factorial of {i} is {fact(i)}")
        
    return fact(n)

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is {fact(number)}")
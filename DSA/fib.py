# Fibonacci using iterative approach
def fibonacci(n):
    if n < 0:
        return "Invalid Input"
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
        
    return curr

# Fibonacci using golden ratio

def fibonacci_golden_ratio(n):
    if n < 0:
        return "Invalid Input"
    
    phi = (1 + (5 ** 0.5)) / 2
    fib_num = ((phi ** n) - ((1-phi) ** n)) / (5 ** 0.5)
    
    return int(round(fib_num))

def fib_sequece(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence

# Example
num = int(input("Enter a number: "))
print(f"Fibonacci Number Using Golden Ratio (Binet's formula): {fibonacci_golden_ratio(num)}")

print(f"Fibonacci Number Using Iterative Approach: {fibonacci(num)}")
print(f"Fibonacci Sequence up to {num}: {fib_sequece(num)}")
# Check if the number is Even/Odd and Prime/Not Prime without using any conditional statements

def even_odd(n):
    result = ['Even','Odd']
    return result[n % 2]

def isprime(n):
    result = ['Composite', 'Prime'] # Not Prime -> Composite
    return result[n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))]


def main():
    while True:
        try:
            num = int(input("Enter Number : "))
            print(f"{num} is {even_odd(num)} and {isprime(num)}")
        except Exception:
            break

if __name__ == "__main__":
    main()
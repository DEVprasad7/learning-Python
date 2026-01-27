from functools import lru_cache

@lru_cache(maxsize=128)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(90))

print(factorial.cache_parameters())
print(factorial.cache_info())
# print(factorial.cache_clear())

@lru_cache()
def fib(n):
    if n <= 1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(999))
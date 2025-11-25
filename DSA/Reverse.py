# Reversing a string or number in Python

def reverse_string(s):
    return s[::-1]

def reverse_number(n):
    n = str(n)
    return int(n[::-1])

def reverse_seq(s):
    return " ".join(s.split()[::-1])


# Example usage
num = 12345
string = "Hello, World!"
print(f"Original number: {num}, Reversed number: {reverse_number(num)}")
print(f"Original string: '{string}', Reversed string: '{reverse_string(string)}'")
print(f"Original sequence: '{string}', Reversed sequence: '{reverse_seq(string)}'")
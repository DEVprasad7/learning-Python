""" A Program to check if a string is palindrome or not """

def is_palindrome(s):
    """ Return True if s is palindrome """
    return s == s[::-1]

def main():
    s = input("Enter a string: ")
    if is_palindrome(s):
        print(s, "is palindrome")
    else:
        print(s, "is not palindrome")

if __name__ == '__main__':
    main()
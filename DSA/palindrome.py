text = input("Enter a string: ")

def palindrome_without_casesensitivity(s):
    normalized_text = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_text == normalized_text[::-1]

def palindrome_with_casesensitivity(s):
    return s == s[::-1]

choice = input("Ignore case sensitivity? (yes/no): ").strip().lower()

if choice == 'yes':
    if palindrome_without_casesensitivity(text):
        print("The string is a palindrome (case insensitive).")
    else:
        print("The string is not a palindrome (case insensitive).")
        
elif choice == 'no':
    if palindrome_with_casesensitivity(text):
        print("The string is a palindrome (case sensitive).")
    else:
        print("The string is not a palindrome (case sensitive).")
        
else:
    print("Invalid choice. Please enter 'yes' or 'no'.")
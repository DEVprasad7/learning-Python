# Desc: This program encrypts and decrypts a string using Caesar cipher hard method
# Can use isaplha() method to check if the character is an alphabet
# Can use ord() to convert character to ASCII value and chr() to convert ASCII value to character easy method.
def main():
    str1 = input("Enter string :")
    lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    shift = int(input("Enter shift :")) # shift is the number of positions to shift the character usually 3
    result = ""
    
    # loops through the string.
    for char in str1: 
        # checks if the character is in the list
        if char in lst:
            # shifts the character by the number of positions
            result = result + lst[(lst.index(char) + shift)]
        else:
            result = result + char


    print("Encrypted string is : ", result)
    print("Decrypted string is : ", str1)





if __name__ == "__main__":
    main()

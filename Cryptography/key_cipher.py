def main():
    # Takes string input from the user
    Text = input("Enter the text: ").strip()
    # Encryption key
    key = "BEST"
    result =""
    i = 0
    for char in Text:
        # checks if the character is not a letter
        if not char.isalpha():
            result += char
            i += 1
            continue
        # checks if the character is upper case or lower case and assigns the ASCII value of the starting letter
        start = ord('A') if char.isupper() else ord('a')
        # ASCII value of the character
        p = ord(char)
        # ASCII value of the key
        k = ord(key[i%len(key)])
        result += chr((p + k) % 26 + start)      
        i += 1  

    print(f"Encrypted : {result} ")



if __name__ == '__main__':
    main()
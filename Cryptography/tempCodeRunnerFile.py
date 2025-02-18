def main():
    try:
        plaintext = input("Enter he text : ").strip().split(" ")
        row = [[], []]
        flag = 0
        for word in plaintext:
            for char in word:
                row[flag%2].append(char)
                flag += 1
        ciphertext = (''.join(row[0])) + (''.join(row[1]))

        print(f"Plain_Text : {''.join(plaintext)}")
        print(f"Cipher_Text : {ciphertext}")
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
# # Encrypting and Decrypting using Transposition Cipher without a key
# # input : "HAPPY NEW YEAR"
# # output : "HPYEYAAPNWER"
def main():
    try:
        plaintext = input("Enter the plaintext : ").strip().split(" ")
        half_1 = ""
        half_2 = ""
        ciphertext = ""
        flag = 0
        for word in plaintext:
            for char in word:
                if flag % 2 == 0:
                    half_1 += char
                else:
                    half_2 += char
                flag += 1
        ciphertext = half_1 + half_2
        print(f"Plain_Text : {''.join(plaintext)}")
        print(f"Cipher_Text : {ciphertext}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
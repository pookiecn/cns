def letter_to_number(letter):
    return ord(letter.lower()) - ord('a')

def number_to_letter(number):
    return chr(number + ord('a'))

def encrypt_vernam(plaintext, key):
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    ciphertext = []
    
    for p, k in zip(plaintext, key):
        if p.isalpha():
            p_num = letter_to_number(p)
            k_num = letter_to_number(k)
            cipher_num = (p_num + k_num) % 26
            ciphertext.append(number_to_letter(cipher_num))
        else:
            ciphertext.append(p)
    
    return ''.join(ciphertext)

def decrypt_vernam(ciphertext, key):
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    plaintext = []
    
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            c_num = letter_to_number(c)
            k_num = letter_to_number(k)
            # Decryption formula: (ciphertext_num - key_num + 26) % 26
            plain_num = (c_num - k_num + 26) % 26
            plaintext.append(number_to_letter(plain_num))
        else:
            plaintext.append(c)
    
    return ''.join(plaintext)

def main():
    action = input("Would you like to encrypt or decrypt? (e/d): ").lower()

    if action == 'e':
        plaintext = input("Enter the plaintext: ")
        key = input("Enter the key: ")
        ciphertext = encrypt_vernam(plaintext, key)
        print("Encrypted ciphertext:", ciphertext)
    elif action == 'd':
        ciphertext = input("Enter the ciphertext: ")
        key = input("Enter the key: ")
        plaintext = decrypt_vernam(ciphertext, key)
        print("Decrypted plaintext:", plaintext)
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")

# Run the program
if __name__ == "__main__":
    main()

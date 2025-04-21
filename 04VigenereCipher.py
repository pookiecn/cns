def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper()
    
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    
    return plaintext

# Get user input for plaintext and key
plaintext = input("Enter the plaintext: ")
key = input("Enter the keyword/key: ")

# Encrypt the plaintext
cipher_text = vigenere_encrypt(plaintext, key)
print("Cipher text: ", cipher_text)

# Decrypt the cipher text
decrypted_text = vigenere_decrypt(cipher_text, key)
print("Decrypted text: ", decrypted_text)

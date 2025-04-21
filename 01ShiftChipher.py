def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result

# Step 1: Get text to encrypt
message = input("Enter the text to encrypt: ")

# Step 2: Get shift key for encryption
encrypt_shift = int(input("Enter the shift key to encrypt: "))
encrypted_text = caesar_cipher(message, encrypt_shift)
print("Encrypted text:", encrypted_text)

# Step 3: Get shift key for decryption
decrypt_shift = int(input("Enter the shift key to decrypt: "))
decrypted_text = caesar_cipher(encrypted_text, -decrypt_shift)
print("Decrypted text:", decrypted_text)

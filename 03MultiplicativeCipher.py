# its not product cipher because it is some different technique.

def encrypt_string(input_string, key):
    encrypted_string = ""
    
    for char in input_string:
        if char.isalpha():
            num = ord(char.lower()) - ord('a')
            
            encrypted_num = (num * key) % 26
            
            encrypted_char = chr(encrypted_num + ord('a'))
            
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    
    return encrypted_string

def find_multiplicative_inverse(key):
    for i in range(26):
        if (key * i) % 26 == 1:
            return i
    return None

def decrypt_string(input_string, key):
    inverse_key = find_multiplicative_inverse(key)
    
    if inverse_key is None:
        raise ValueError(f"No multiplicative inverse exists for the key {key}.")
    
    decrypted_string = ""
    
    for char in input_string:
        if char.isalpha():
            num = ord(char.lower()) - ord('a')
            
            decrypted_num = (num * inverse_key) % 26
            
            decrypted_char = chr(decrypted_num + ord('a'))
            
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted_string += decrypted_char
        else:
            decrypted_string += char
    
    return decrypted_string

input_string = input("Enter the string : ")
key = int(input("Enter the key: "))
option = int(input("1 : Encrytion\n2 : Decryption\n> "))

if option == 1:
    output_string = encrypt_string(input_string, key)
elif option == 2:
    output_string = decrypt_string(input_string, key)
else:
    option = int(input("Enter valid Integer "))

print("Result string: ", output_string)

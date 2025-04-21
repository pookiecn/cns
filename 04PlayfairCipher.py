def create_playfair_matrix(key):
    # Remove duplicates from the key and remove 'J' (treat 'J' as 'I')
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicate characters from key
    key = key.replace('J', 'I')  # Treat 'J' as 'I'
    
    # Create matrix of 5x5
    matrix = []
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return matrix

def prepare_text(text):
    # Replace all non-alphabetic characters
    text = ''.join([char.upper() for char in text if char.isalpha()])
    text = text.replace('J', 'I')  # Treat 'J' as 'I'

    # Split text into digraphs
    digraphs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            digraphs.append(text[i:i + 2])
            i += 2
        else:
            digraphs.append(text[i] + 'X')  # If the same letter, add 'X' in between
            i += 1
    
    return digraphs

def find_position(char, matrix):
    # Find the position (row, column) of a character in the matrix
    index = matrix.index(char)
    row = index // 5
    col = index % 5
    return row, col

def encrypt_playfair(plaintext, key):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_text(plaintext)
    cipher_text = ""
    
    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)
        
        if row1 == row2:
            cipher_text += matrix[row1 * 5 + (col1 + 1) % 5]
            cipher_text += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[((row1 + 1) % 5) * 5 + col1]
            cipher_text += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            cipher_text += matrix[row1 * 5 + col2]
            cipher_text += matrix[row2 * 5 + col1]
    
    return cipher_text

def decrypt_playfair(ciphertext, key):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_text(ciphertext)
    plaintext = ""
    
    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)
        
        if row1 == row2:
            plaintext += matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += matrix[row1 * 5 + col2]
            plaintext += matrix[row2 * 5 + col1]
    
    return plaintext.replace('X', '')

# Get user input for plaintext and key
plaintext = input("Enter the plaintext: ")
key = input("Enter the keyword/key: ")

# Encrypt the plaintext
cipher_text = encrypt_playfair(plaintext, key)
print("Cipher text: ", cipher_text)

# Decrypt the cipher text
decrypted_text = decrypt_playfair(cipher_text, key)
print("Decrypted text: ", decrypted_text)

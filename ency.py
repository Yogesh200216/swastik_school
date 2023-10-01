def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shift = ord('a' if char.islower() else 'A')
            encrypted_char = chr((ord(char) - shift + key) % 23 + shift)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Get user input for message and key
message = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key: "))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

input("Press Enter to Exit")
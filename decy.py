def decrypt(encrypted_message, key):
    decrypted_message = ''
    for char in encrypted_message:
        if char.isalpha():
            shift = ord('a' if char.islower() else 'A')
            decrypted_char = chr((ord(char) - shift - key) % 23 + shift)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message
    

encrypted_message = input("Enter Encrypted Message :- ")
key = int(input("Enter the key :- "))
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
input("Press Enter to Exit")
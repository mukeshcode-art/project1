def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")
        return

    text = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

    result = caesar_cipher_encrypt(text, shift) if choice == 'e' else caesar_cipher_decrypt(text, shift)
    action = "Encrypted" if choice == 'e' else "Decrypted"
    print(f"{action} message: {result}")

if __name__ == "__main__":
    main()
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')            
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:          
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter text: ")
shift_amt = int(input("Enter shift count: "))
encrypted_text = caesar_cipher(plaintext, shift_amt)
print("Original:", plaintext)
print("Encrypted:", encrypted_text)

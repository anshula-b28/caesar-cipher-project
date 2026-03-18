#Encryption
def encrypt(message,shift):
    encrypted=""
    for char in message:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            encrypted+=chr((ord(char)-base+shift)%26+base)
        else:
            encrypted+=char
    return encrypted
#Decryption
def decrypt(ciphertext,shift):
    decrypted=""
    for char in ciphertext:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            decrypted+=chr((ord(char)-base-shift)%26+base)
        else:
            decrypted+=char
    return decrypted
#Main Program
message=input("Enter the message:")
shift=int(input("Enter shift value:"))

encrypted_text=encrypt(message,shift)
print("Encrypted Message:",encrypted_text)

decrypted_text=decrypt(encrypted_text,shift)
print("Decrypted Message:",decrypted_text)

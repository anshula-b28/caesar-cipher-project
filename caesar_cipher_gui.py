import tkinter as tk
from tkinter import messagebox

# Encryption
def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Decryption
def decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# GUI Functions
def encrypt_text():
    message = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted = encrypt(message, shift)
        encrypted_text.delete("1.0", tk.END)
        encrypted_text.insert(tk.END, encrypted)
        # Also show decrypted automatically
        decrypted_text.delete("1.0", tk.END)
        decrypted_text.insert(tk.END, decrypt(encrypted, shift))
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("500x500")

# Input
tk.Label(root, text="Enter Message:").pack()
input_text = tk.Text(root, height=2)
input_text.pack()

tk.Label(root, text="Enter Shift:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Buttons
tk.Button(root, text="Encrypt & Decrypt", command=encrypt_text).pack(pady=10)

# Encrypted output
tk.Label(root, text="Encrypted Text:").pack()
encrypted_text = tk.Text(root, height=2)
encrypted_text.pack()

# Decrypted output
tk.Label(root, text="Decrypted Text:").pack()
decrypted_text = tk.Text(root, height=2)
decrypted_text.pack()

root.mainloop()
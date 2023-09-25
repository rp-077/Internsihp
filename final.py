import tkinter as tk
from tkinter import ttk

def encrypt(text, shift):
    # Caesar Cipher encryption logic here
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
            if char.isupper():
                encrypted_text += chr(ord('A') + shift_amount)
            else:
                encrypted_text += chr(ord('a') + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    # Caesar Cipher decryption logic here
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') - shift) % 26
            if char.isupper():
                decrypted_text += chr(ord('A') + shift_amount)
            else:
                decrypted_text += chr(ord('a') + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    def encrypt_text():
        text = text_entry.get()
        shift = int(shift_entry.get())
        encrypted_text = encrypt(text, shift)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, encrypted_text)

    def decrypt_text():
        text = text_entry.get()
        shift = int(shift_entry.get())
        decrypted_text = decrypt(text, shift)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, decrypted_text)

    window = tk.Tk()
    window.title("Caesar Cipher Encryption and Decryption")

    label = ttk.Label(window, text="Choose an option:")

    choice = tk.StringVar()
    
    

    text_label = ttk.Label(window, text="Enter text:")
    text_entry = ttk.Entry(window)

    shift_label = ttk.Label(window, text="Enter shift value:")
    shift_entry = ttk.Entry(window)

    encrypt_button = ttk.Button(window, text="Encrypt")
    decrypt_button = ttk.Button(window, text="Decrypt")

    result_text = tk.Text(window, height=5, width=40)

    label.grid(row=0, column=0, columnspan=2)
    
    text_label.grid(row=2, column=0)
    text_entry.grid(row=2, column=1)
    shift_label.grid(row=3, column=0)
    shift_entry.grid(row=3, column=1)
    encrypt_button.grid(row=4, column=0)
    decrypt_button.grid(row=4, column=1)
    result_text.grid(row=5, column=0, columnspan=2)

    encrypt_button.config(command=encrypt_text)
    decrypt_button.config(command=decrypt_text)

    window.mainloop()

if __name__ == "__main__":
    main()

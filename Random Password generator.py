import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Password Length:", font=("Arial", 10)).pack()
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.insert(0, "12")
        self.length_entry.pack(pady=5)

        self.include_letters = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        
        tk.Checkbutton(root, text="Include Letters", variable=self.include_letters).pack()
        tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers).pack()
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
        self.result_label.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 10), bg="#2196F3", fg="white", state="disabled")
        self.copy_button.pack(pady=5)

    def generate_password(self):
        """Generates a password based on user-selected options."""
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than 0.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for password length.")
            return

        character_pool = ""
        if self.include_letters.get():
            character_pool += string.ascii_letters
        if self.include_numbers.get():
            character_pool += string.digits
        if self.include_symbols.get():
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showwarning("Selection Error", "Select at least one character type!")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.result_label.config(text=password)
        
        self.copy_button.config(state="normal")

    def copy_to_clipboard(self):
        password = self.result_label.cget("text")
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
        
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()

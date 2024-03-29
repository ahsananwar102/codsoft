import tkinter as tk
from tkinter import messagebox
import random
import string as str

# FUNCTION DEFINITIONS

def password_generator():
    try:
        length = int(num_box.get()) # Getting the length entered by the user
        
        if length >= 4 and length <= 40:
            char = str.ascii_letters + str.digits + str.punctuation
            password = "" 
            for i in range(length):
                password += random.choice(char)

            pass_text.config(text=password, highlightthickness=2, highlightbackground="#BAC5C9", padx=20, font=("Arial", "13", "bold"))

            # Password copied message
            copy_button.pack(padx=10, pady=10)
            message_label.pack()
        else:
            messagebox.showwarning("Warning", "The length should be greater than 4 and less than 40") 

    except:
        messagebox.showwarning("Warning", "Enter a valid number!") 

def copy_password():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(textbox_label2.cget("text"))  # Append the text to the clipboard
    root.update()  # Update the clipboard
    message_label.config(text="Password copied to clipboard ✔", fg="lightgreen", bg= color)
    root.after(3000, clear_message)

def clear_message():
    message_label.config(text="")  # Clear the message label

color = "#232B31"

root = tk.Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
main = tk.Frame(root, bg=color) # Setting the main frame
main.pack(fill="both", expand=True)

root.title("Password Generator")
label = tk.Label(main, text="Password Generator", font=("Cambria", "28", "bold"), bg=color, fg="white")
label.pack(fill="x",padx=10, pady=(30, 0))

# Separator after the main heading
separator1 = tk.Frame(main, bd=10, relief='sunken', height=4)
separator1.pack(side='top', fill='x', padx=20, pady=(20, 30))

textbox_label = tk.Label(main, text="Specify the length of password:", font=("Courier", 13), anchor="w", bg=color, fg="white")
textbox_label.pack(padx=10, pady=10)

# Input box for the the length of the password
num_box = tk.Spinbox(main, font=("Courier", "13", "bold"), from_=8, to=100)
num_box.pack(padx=10)

# Submit Button
submit_button = tk.Button(main, text="Submit", command=password_generator, anchor="center", font=("Arial", "14"), width=10, height = 1, border=2, cursor = "hand2")
submit_button.pack(pady=20)

textbox_label2 = tk.Label(main, text="Generated password:", font=("Courier", 18, "bold"), anchor="w", bg=color, fg="white")
textbox_label2.pack(padx=10, pady=(20, 10))

# Label for the generated password
pass_text = tk.Label(main, font=("Courier", "12"), anchor="center", border=10, text="(Password will appear here)", bg=color, fg="white")
pass_text.pack()

# Copy Password Button
copy_button = tk.Button(main, text="Copy Password", command=copy_password, font=("Arial", "11"))

# Label for "Copied to clipboard" message
message_label = tk.Label(main, fg="green",  font=("Segoe UI Symbol", 8), bg=color)

root.mainloop()

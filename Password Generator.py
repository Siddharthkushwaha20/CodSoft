import tkinter as tk
from tkinter import ttk
import random
import string


# Function to generate a random password
def generate_password(length, complexity):
    if complexity == "Easy":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "Hard":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to update the password label
def update_password():
    password_length = int(length_entry.get())
    password_complexity = complexity_var.get()
    generated_password = generate_password(password_length, password_complexity)
    password_label.config(text=generated_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("800x600")

# Create a frame for the content
content_frame = ttk.Frame(root)
content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create and configure widgets
length_label = ttk.Label(content_frame, text="Password Length:", font=("Arial", 16))
length_label.grid(row=0, column=0, sticky='w', pady=(0, 10))

length_entry = ttk.Entry(content_frame, font=("Arial", 16))
length_entry.grid(row=0, column=1, pady=(0, 10))

complexity_label = ttk.Label(content_frame, text="Password Complexity:", font=("Arial", 16))
complexity_label.grid(row=1, column=0, sticky='w', pady=(0, 10))

complexity_var = tk.StringVar()
complexity_var.set("Easy")

complexity_options = ["Easy", "Medium", "Hard"]
complexity_menu = ttk.Combobox(content_frame, textvariable=complexity_var, values=complexity_options, font=("Arial", 16))
complexity_menu.grid(row=1, column=1, pady=(0, 10))

generate_button = ttk.Button(content_frame, text="Generate Password", command=update_password, style='TButton', width=20)
generate_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

password_label = ttk.Label(content_frame, text="", font=("Arial", 16, "bold"))
password_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

password_get=ttk.Label(content_frame, text="", font=("Arial",16,"bold"))
password_get.grid(row=3)

# Start the GUI main loop
root.mainloop()




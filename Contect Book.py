import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Error", "Please provide at least a name and a phone number.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_listbox.insert(tk.END, f'{name}: {details["phone"]}')

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def view_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        name = contact_listbox.get(index).split(":")[0].strip()
        details = contacts[name]
        messagebox.showinfo(name, f'Phone: {details["phone"]}\nEmail: {details["email"]}\nAddress: {details["address"]}')
    else:
        messagebox.showwarning("No Selection", "Please select a contact.")

def search_contact():
    search_term = search_entry.get().lower()
    search_result.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details['phone']:
            search_result.insert(tk.END, f'{name}: {details["phone"]}')

def delete_contact():
    selected_contact = search_result.curselection()
    if selected_contact:
        index = selected_contact[0]
        name = search_result.get(index).split(":")[0].strip()
        del contacts[name]
        update_contact_list()
        search_contact()
    else:
        messagebox.showwarning("No Selection", "Please select a contact.")

# Create the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("800x600")

# Create and configure widgets
frame = tk.Frame(root)
frame.pack(padx=140, pady=80, fill='both', expand=True)

tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Phone:").grid(row=1, column=0, sticky='e')
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Email:").grid(row=2, column=0, sticky='e')
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Address:").grid(row=3, column=0, sticky='e')
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

contact_listbox = tk.Listbox(frame, width=40)
contact_listbox.grid(row=0, column=2, rowspan=5, padx=20)
update_contact_list()

view_button = tk.Button(frame, text="View Contact", command=view_contact)
view_button.grid(row=5, column=0, pady=(0, 10))

search_label = tk.Label(frame, text="Search:")
search_label.grid(row=6, column=0, pady=(0, 10))
search_entry = tk.Entry(frame)
search_entry.grid(row=6, column=1, pady=(0, 10))
search_button = tk.Button(frame, text="Search", command=search_contact)
search_button.grid(row=6, column=2, pady=(0, 10))

search_result = tk.Listbox(frame, width=40)
search_result.grid(row=7, column=2, padx=20)
search_contact()

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=0, pady=(0, 10))

root.mainloop()

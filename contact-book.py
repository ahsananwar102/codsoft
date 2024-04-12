import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Function to add a contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()
    if name == '' or number == '' or email == '':
        messagebox.showerror("Error", "Please enter all fields")
        return
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, number, email])
    messagebox.showinfo("Success", "Contact added successfully")
    clear_entries()
    display_contacts()

# Function to update a contact
def update_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()
    if name == '' or number == '' or email == '':
        messagebox.showerror("Error", "Please enter all fields")
        return
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        found = False
        for i, row in enumerate(rows):
            if row[0] == name:
                rows[i] = [name, number, email]
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found")
            return
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    messagebox.showinfo("Success", "Contact updated successfully")
    clear_entries()
    display_contacts()

# Function to delete a contact
def delete_contact():
    name = name_entry.get()
    if name == '':
        messagebox.showerror("Error", "Please enter a name")
        return
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        found = False
        for i, row in enumerate(rows):
            if row[0] == name:
                del rows[i]
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found")
            return
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    messagebox.showinfo("Success", "Contact deleted successfully")
    clear_entries()
    display_contacts()

# Function to display contacts
def display_contacts():
    for row in contact_treeview.get_children():
        contact_treeview.delete(row)
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contact_treeview.insert('', 'end', values=row)

# Function to handle selection of a contact
def on_select(event):
    selected_contact = contact_treeview.focus()
    if selected_contact:
        contact_details = contact_treeview.item(selected_contact)['values']
        name, number, email = contact_details
        name_entry.delete(0, END)
        name_entry.insert(END, name)
        number_entry.delete(0, END)
        number_entry.insert(END, number)
        email_entry.delete(0, END)
        email_entry.insert(END, email)

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, END)
    number_entry.delete(0, END)
    email_entry.delete(0, END)

# Main Tkinter window
root = Tk()
root.title("Contact Book")
root.geometry("600x450")

# Heading
Label(root, text="Contact Book", font=("Arial", 20, "bold"), padx=10, pady=10).grid(row=0, column=0, columnspan=2, pady=15)

# Labels
Label(root, text="Name:").grid(row=1, column=0, padx=15, pady=5, sticky='w')
Label(root, text="Number:").grid(row=2, column=0, padx=15, pady=5, sticky='w')
Label(root, text="Email:").grid(row=3, column=0, padx=15, pady=5, sticky='w')

# Entry fields
name_entry = Entry(root, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=5)
number_entry = Entry(root, width=40)
number_entry.grid(row=2, column=1, padx=10, pady=5)
email_entry = Entry(root, width=40)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons frame
buttons_frame = Frame(root)
buttons_frame.grid(row=4, column=0, columnspan=2, pady=10)

# Buttons
Button(buttons_frame, text="Add Contact", command=add_contact, width=15).pack(side=LEFT, padx=5)
Button(buttons_frame, text="Update Contact", command=update_contact, width=15).pack(side=LEFT, padx=5)
Button(buttons_frame, text="Delete Contact", command=delete_contact, width=15).pack(side=LEFT, padx=5)

# TreeView to display contacts
columns = ('Name', 'Number', 'Email')
contact_treeview = ttk.Treeview(root, columns=columns, show='headings', selectmode='browse')
for col in columns:
    contact_treeview.heading(col, text=col)
contact_treeview.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
contact_treeview.bind('<<TreeviewSelect>>', on_select)

# Scrollbar for TreeView
scrollbar = Scrollbar(root, orient="vertical", command=contact_treeview.yview)
scrollbar.grid(row=5, column=2, sticky='ns')
contact_treeview.configure(yscrollcommand=scrollbar.set)

# Configure column and row to expand with the window
root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)

# Display saved contacts
display_contacts()

root.mainloop()


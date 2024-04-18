import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        add_button.grid(row=1, column=0, padx=5, pady=5)

        search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        search_button.grid(row=1, column=1, padx=5, pady=5)

        view_button = tk.Button(self.root, text="View All Contacts", command=self.view_contacts)
        view_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        update_button.grid(row=3, column=0, padx=5, pady=5)

        delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        delete_button.grid(row=3, column=1, padx=5, pady=5)

    def add_contact(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")

        tk.Label(add_window, text="Name:").grid(row=0, column=0)
        tk.Label(add_window, text="Phone Number:").grid(row=1, column=0)
        tk.Label(add_window, text="Email:").grid(row=2, column=0)
        tk.Label(add_window, text="Address:").grid(row=3, column=0)

        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1)
        phone_entry = tk.Entry(add_window)
        phone_entry.grid(row=1, column=1)
        email_entry = tk.Entry(add_window)
        email_entry.grid(row=2, column=1)
        address_entry = tk.Entry(add_window)
        address_entry.grid(row=3, column=1)

        add_button = tk.Button(add_window, text="Add", command=lambda: self.save_contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), add_window))
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_contact(self, name, phone_number, email, address, add_window):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        add_window.destroy()
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Contact")

        tk.Label(search_window, text="Search:").grid(row=0, column=0)
        search_entry = tk.Entry(search_window)
        search_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search", command=lambda: self.perform_search(search_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def perform_search(self, search_term, search_window):
        search_window.destroy()
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        if not search_results:
            messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            result_string = "\n".join([f"Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\n" for contact in search_results])
            messagebox.showinfo("Search Results", result_string)

    def update_contact(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Error", "Please select a contact to update.")
        else:
            index = selection[0]
            contact = self.contacts[index]
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Contact")

            tk.Label(update_window, text="Name:").grid(row=0, column=0)
            tk.Label(update_window, text="Phone Number:").grid(row=1, column=0)
            tk.Label(update_window, text="Email:").grid(row=2, column=0)
            tk.Label(update_window, text="Address:").grid(row=3, column=0)

            name_entry = tk.Entry(update_window)
            name_entry.grid(row=0, column=1)
            name_entry.insert(tk.END, contact.name)
            phone_entry = tk.Entry(update_window)
            phone_entry.grid(row=1, column=1)
            phone_entry.insert(tk.END, contact.phone_number)
            email_entry = tk.Entry(update_window)
            email_entry.grid(row=2, column=1)
            email_entry.insert(tk.END, contact.email)
            address_entry = tk.Entry(update_window)
            address_entry.grid(row=3, column=1)
            address_entry.insert(tk.END, contact.address)

            update_button = tk.Button(update_window, text="Update", command=lambda: self.save_updated_contact(index, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), update_window))
            update_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_updated_contact(self, index, name, phone_number, email, address, update_window):
        contact = Contact(name, phone_number, email, address)
        self.contacts[index] = contact
        update_window.destroy()
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Error", "Please select a contact to delete.")
        else:
            index = selection[0]
            del self.contacts[index]
            self.listbox.delete(index)
            messagebox.showinfo("Success", "Contact deleted successfully.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

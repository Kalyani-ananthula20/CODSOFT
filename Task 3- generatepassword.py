import random
import string
import tkinter as tk

def generate_password():
    password_length = int(length_entry.get())
    
    if include_symbols.get():
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
        
    password = ''.join(random.choice(characters) for i in range(password_length))
    result_label.config(text=password)

window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200") 

length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window, width=25)  
length_entry.grid(row=0, column=1, padx=10, pady=5)

include_symbols = tk.BooleanVar()
include_symbols.set(True)
symbol_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=include_symbols)
symbol_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, width=30)  
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="", width=30, height=3, wraplength=250)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()

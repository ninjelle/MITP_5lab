import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select file",
        filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py")
        ]
    )
    
    if file_path:
        file_label.config(text=f"Selected: {file_path}")
        
        import os
        filename = os.path.basename(file_path)
        name_label.config(text=f"File name: {filename}")

root = tk.Tk()
root.title("File Dialog Example")
root.geometry("500x200") 

select_button = tk.Button(
    root, 
    text="📁 Select file", 
    command=open_file,
    font=("Arial", 12),
    bg="pink",
    padx=10,
    pady=5
)
select_button.pack(pady=20)

file_label = tk.Label(
    root,
    text="No file selected",
    font=("Arial", 10),
    fg="gray",
    wraplength=450
)
file_label.pack(pady=10)

name_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    fg="deeppink"
)
name_label.pack(pady=5)

root.mainloop()
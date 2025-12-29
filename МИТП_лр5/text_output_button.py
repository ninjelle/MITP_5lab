import tkinter as tk
from tkinter import ttk

def show_text():
    input_text = entry.get() 
    label_result.config(text=f"Your text: {input_text}")  

root = tk.Tk()
root.title("Text")
root.geometry("400x200")

entry = ttk.Entry(root, width=30)
entry.pack(pady=20)

button = ttk.Button(root, text="Output text", command=show_text)
button.pack()

label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()

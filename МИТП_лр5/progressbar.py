import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    start_button.config(state=tk.DISABLED)
    
    progress_bar['value'] = 0
    
    root.update_idletasks()
    
    for i in range(1, 101):  
        progress_bar['value'] = i 
        percent_label.config(text=f"{i}%") 
        root.update()  
        time.sleep(0.03)  
    
    start_button.config(state=tk.NORMAL)
    
    percent_label.config(text="Ready!")

root = tk.Tk()
root.title("Progress bar")
root.geometry("400x150")

progress_bar = ttk.Progressbar(
    root, 
    length=300, 
    mode='determinate', 
    maximum=100  
)
progress_bar.pack(pady=20)

percent_label = ttk.Label(root, text="0%", font=("Arial", 14))
percent_label.pack()

start_button = ttk.Button(
    root, 
    text="Start", 
    command=start_progress
)
start_button.pack(pady=10)

root.mainloop()

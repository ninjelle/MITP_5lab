import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot():
    ax.clear()
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    ax.plot(x, y, 'r-', linewidth=2)
    ax.set_title("Graph sin(x)")
    ax.grid(True)
    
    canvas.draw()

root = tk.Tk()
root.title("Graph")
root.geometry("1500x1000")

fig, ax = plt.subplots(figsize=(5, 3), dpi=100)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

plot_button = tk.Button(
    button_frame,
    text="PLOT GRAPH",  
    command=plot,
    font=("Arial", 14, "bold"),
    bg="pink", 
    fg="deeppink", 
    padx=30,  
    pady=15,  
    borderwidth=3,    
    cursor="hand2"   
)
plot_button.pack()

root.mainloop()

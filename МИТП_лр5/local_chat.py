import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Cool chat")
window.geometry("300x400")

chat_text = tk.Text(window, height=15, width=35, state='disabled')
chat_text.pack(pady=10)

chat_text.tag_configure("pink", foreground="deeppink")

def add_msg(text):
    chat_text.config(state='normal')
    time = datetime.now().strftime("%H:%M")
    if text.startswith("You:"):
        chat_text.insert(tk.END, f"[{time}] {text}\n", "pink")
    else:
        chat_text.insert(tk.END, f"[{time}] {text}\n")
    chat_text.config(state='disabled')
    chat_text.see(tk.END)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)
entry.bind('<Return>', lambda e: send_msg())

def send_msg():
    msg = entry.get()
    
    if msg:
        add_msg(f"You: {msg}")
        entry.delete(0, tk.END)
        
        msg_clean = msg.strip()  
        
        if msg_clean.lower() == "hi":
            add_msg("Bot: Hello! 😊")
        elif msg_clean.lower() == "how are you?":
            add_msg("Bot: I'm fine! 😊")
        else:
            add_msg("Bot: I don't understand...")

tk.Button(
    window, 
    text="Send", 
    command=send_msg,
    bg="pink"  
).pack()

add_msg("Start chatting!")
window.mainloop()